# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import simplejson as json
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

def get(url, header):
    # request headers
    req = urllib2.Request(url, None, header)
    req_header_get = req.header_items()
    print "***request header_get = ***\n%s" % req_header_get

    # send request and get response handle
    res = urllib2.urlopen(req)

    # response code
    res_code = res.getcode()
    print "***response code = ***\n%s" % res_code
    # response header
    res_header = res.info()
    print "***response header = ***\n%s" % res_header
    # response body
    res_body = res.read()
    print "***response body = ***\n%s" % res_body
    res.close()

    return res_body

def post(url, data, header):
    #request headers

    print "MARK MARK MARK--- ", url," ---MARK MARK MARK"
    print "MARK MARK MARK--- ", data, " ---MARK MARK MARK"
    print "MARK MARK MARK--- ", header, " ---MARK MARK MARK"

    req_header = header

    #request body
    data = urllib.urlencode(data)

    #pre--request
    req = urllib2.Request(url, data, req_header)

    #req_header_tmp = req.get_header("User-agent")
    #print "***request header_tmp = *** %s" % req_header_tmp

    req_header_get = req.header_items()
    print "***request header_get = ***\n%s" % req_header_get

    req_body = req.get_data()
    print "***request body = ***\n%s" % req_body
    #send request and get response handle
    res = urllib2.urlopen(req)

    #response code
    res_code = res.getcode()
    print "***response code = ***\n%s" % res_code
    #response header
    res_header = res.info()
    print "***response header = ***\n%s" % res_header
    #response body
    res_body =  res.read()
    print "***response body = ***\n%s" % res_body
    res.close()

    return res_body

def post_upload_file(url, file, header):
    #此方法用于上传文件接口的post形式
    # request headers
    print "@@@ header input is", header

    # 在 urllib2 上注册 http 流处理句柄
    register_openers()
    ######判断上传的文件是否为空（在异常逻辑中--文件为空接口中用到）######################
    if(file == ""):
        data,header_ext = multipart_encode({"files":""})
    else:
        data, header_ext = multipart_encode({"files":open(file,"rb")})

    header.update(header_ext)

    # pre--request
    req = urllib2.Request(url, data, header)

    req_header_get = req.header_items()
    print "***request header_get = ***\n%s" % req_header_get

    # send request and get response handle
    res = urllib2.urlopen(req)

    # response code
    res_code = res.getcode()
    print "***response code = ***\n%s" % res_code
    # response header
    res_header = res.info()
    print "***response header = ***\n%s" % res_header
    # response body
    res_body = res.read()
    print "***response body = ***\n%s" % res_body
    res.close()

    return res_body

def post_json(url, data, header):
    #request headers

    print "MARK MARK MARK---URL----- ", url," ---MARK MARK MARK"
    print "MARK MARK MARK---DATA____ ", data, " ---MARK MARK MARK"
    print "MARK MARK MARK---HEADER___ ", header, " ---MARK MARK MARK"


    #request body
    # data = urllib.urlencode(data)
    data = json.dumps(data)

    #pre--request

    req = urllib2.Request(url, data,header)

    req_body = req.get_data()
    print "***request body = ***\n%s" % req_body
    #send request and get response handle
    res = urllib2.urlopen(req)

    #response code
    res_code = res.getcode()
    print "***response code = ***\n%s" % res_code
    #response header
    res_header = res.info()
    print "***response header = ***\n%s" % res_header
    #response body
    res_body =  res.read()
    print "***response body = ***\n%s" % res_body
    res.close()

    return res_body
#************************************************************************************
def mylogin():
    # 登录用如下这个接口
    url_login = 'https://www.iumer.cn/umer/webService/personnel/sys/user/login'

    # 自定义请求头
    header_login ={"Content-type": "application/json;charset=UTF-8","X-Type":"2"}

    # 访问登录页面
    data_login = {'phone':'15651966757', 'password':'0adc3949ba59abbe56e057f20f883ee1'}
    res = post_json(url_login,data_login, header_login)

    return null2None2dict(res)

def null2None2dict(res=""):
    res = res.replace("null", "None")
    res = res.replace("false", "False")
    res = res.replace("true", "True")
    return eval(res)
#******************************************3.1*************************************************
#3.1.1
def register(url = "",phone="",password= "",authCode ="",X_Type="2"):
    url = url
    data ={"phone":phone,"password":password,"authCode":authCode}
    header = {"Content-type": "application/json;charset=UTF-8","X-Type":"2"}
    res = post_json(url,data,header)
    return null2None2dict(res)
#3.1.2
def login(url="",phone ="",password="",X_Type="2"):
    url = url
    data = {"phone":phone,"password":password}
    header = {"Content-type": "application/json;charset=UTF-8","X-Type":"2"}
    res = post_json(url,data,header)
    return null2None2dict(res)
#3.1.3
def acceptInvitation(url = "",id ="",businessId="",X_Type="2"):
    url = url
    data = {"id":id,"businessId":businessId}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2","X-Token":token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.1.4
def personnelInfo(url ="",id= "",X_Type = "2"):
    url = url
    data  = {"id":id}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.1.5
def updateInfo(url= "",id = "",name="",sex="",X_Type="2",files=""):
    url = url
    file = files
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token'],
              "id":id,"name":name,"sex":sex}
    res = post_upload_file(url,file,header)
    return  null2None2dict(res)
#3.1.6
def workTime(url = "",id = "", monStart ="",monEnd="",tueStart="",tueEnd="",wedStart="",
    wedEnd="",thuStart="",thuEnd="",friStart="",friEnd="",satStart="",satEnd="",sunStart="",sunEnd="",
    ifMonWork="",ifTueWork="",ifWedWork="",ifThuWork="",ifFriWork="",ifSatWork="",ifSunWork="",X_Type="2"):

    url = url
    data = {"monStart":monStart,"monEnd":monEnd,"tueStart":tueStart,"tueEnd":tueEnd,
            "wedStart":wedStart,"wedEnd":wedEnd,"thuStart":thuStart,"thuEnd":tueEnd,"friStart":friStart,"friEnd":friEnd,
            "satStart":satStart,"satEnd":satEnd,"sunStart":sunStart,"sunEnd":sunEnd,"ifMonWork":ifMonWork,"ifTueWork":ifTueWork,"ifWedWork":ifWedWork,
            "ifThuWork":ifThuWork,"ifFriWork":ifFriWork,"ifSatWork":ifSatWork,"ifSunWork":ifSunWork}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.1.7
def getWorkTime(url ="",personnelId ="",X_Type="2"):
    url = url
    data = {"personnelId":personnelId}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.1.8
def shopInfo(url = "",shopId= "",X_Type = "2"):
    url = url
    data = {"shopId":shopId}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.1.9
def updateRegistrationId(url = "",id="",registrationId="",X_Type="2"):
    url = url
    data = {"id":id,"registrationId":registrationId}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#**********************************3.2*****************************************
#3.2.1
def projecList(url = "",shopId ="",personnelId="",pageSize="",X_Type="2"):
    url = url
    data = {"shopId":shopId,"personnelId":personnelId,"pageSize":pageSize}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.2.2
def chooseProject(url ="",projectIds ="",personnelId="",X_Type = "2"):
    url = url
    data = {"projectIds":projectIds,"personnelId":personnelId}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.2.3
def myProjectList(url = "",shopId= "",personnelId="",pageSize="",X_Type =""):
    url = url
    data = {"shopId":shopId,"personnelId":personnelId,"pageSize":pageSize}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.2.4
def delProject(url = "",projectIds ="",personnelId="",X_Type= "2"):
    url = url
    data = {"projectIds":projectIds,"personnelId":personnelId}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.2.5
def projectDetails(url ="",id ="",X_Type =""):
    url = url
    data = {"id":id}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#***********************************3.3************************************
#3.3.1
def orderGroupNum(url = "",shopId ="",personnelId="",X_Typ ="2"):
    url = url
    data = {"shopId":shopId,"personnelId":personnelId}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.3.2
def myOrderList(url ="",shopId= "",personnelId="",pageSize= "",X_Type ="2"):
    url = url
    data = {"shopId": shopId, "personnelId": personnelId,"pageSize":pageSize}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.3.3
def orderDetail(url="",personnelId="",orderNo="",X_Type= ""):
    url = url
    data= {"personnelId":personnelId,"orderNo":orderNo}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.3.4
def cancelOrder(url ="",personnelId="",orderNo="",X_Type="2"):
    url = url
    data = {"personnelId":personnelId,"orderNo":orderNo}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.3.5
def confirmFinishOrder(url = "",personnelId="",orderNo="",X_Type="2"):
    url = url
    data = {"personnelId": personnelId, "orderNo": orderNo}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.3.5
def scanFinishOrder(url = "",personnelId="",payCode="",X_Type="2"):
    url = url
    data = {"personnelId": personnelId, "payCode":payCode}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.3.6
def orderSave(url ="",projectId = "",personnelId = "",makeStartDate="",makeEndDate="",priceType="",reserveName="",
              reservePhone="",X_Type = "2"):
    url = url;
    data ={"projectId":projectId,"personnelId":personnelId,"makeStartDate":makeStartDate,"makeEndDate":makeEndDate,
            "priceType":priceType,"reserveName":reserveName,"reservePhone":reservePhone}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#***********************************************3.4************************************************
#3.4.1
def customerList(url ="",shopId = "",personnelId="",pageSize="",X_Type=""):
    url = url
    data= {"shopId":shopId,"personnelId":personnelId,"pageSize":pageSize}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.4.2
def changeRemark(url="",shopId="",personnelId="",remark="",customerId="",X_Type=""):
    url = url
    data = {"shopId":shopId,'personnelId':personnelId,"remark":remark,"customerId":customerId}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.4.3
def changeRank(url = "",shopId = "",rankId ="",customerIds="",X_Type ="2"):
    url = url
    data = {"shopId":shopId,"rankId":rankId,"customerIds":customerIds}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.4.4
def customerDetails(url ="",shopId = "",customerId ="",X_Type="2"):
    url = url
    data = {"shopId":shopId,"customerId":customerId}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.4.5
def expenseRecord(url ="",customerId ="",shopId ="",pageSize ="",X_Type="2"):
    url = url
    data = {"customerId":customerId,"shopId":shopId,"pageSize":pageSize}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.4.6
def expenseProject(url="",customerId ="",shopId= "",pageSize="",X_Type ="2"):
    url = url
    data = {"customerId":customerId,"shopId":shopId,"pageSize":pageSize}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.4.7
def rankInfoList(url ="",shopId="",personnelId ="",X_Type ="2"):
    url = url
    data = {"shopId":shopId,"personnelId":personnelId}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.4.8.1
def createCard(url="",shopId="",personnelId="",customerId="",cardType="",name="",remark="",validityDate="",X_Type="2"):
    url = url
    data = {"shopId":shopId,"personnelId":personnelId,"customerId":customerId,"cardType":cardType,
            "name":name,"remark":remark,"validityDate":validityDate}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
# 3.4.8.2
def editCard(url="",shopId="",personnelId="",customerId="",cardType="",id="",name="",remark="",validityDate="",X_Type="2"):
    url = url
    data = {"shopId":shopId,"personnelId":personnelId,"customerId":customerId,"cardType":cardType,"id":id,
            "name":name,"remark":remark,"validityDate":validityDate}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
# 3.4.8.3
def cardDetail(url="",cardId="",X_Type="2"):
    url = url
    data = {"cardId":cardId}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
# 3.4.8.4
def customerCardList(url="",shopId="",customerId="",pageSize="",X_Type = "2"):
    url = url
    data ={"shopId":shopId,"customerId":customerId,"pageSize":pageSize}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
# 3.4.8.5
def operationCard(url="",shopId = "",personnelId="",customerId="",cardType="",id ="",deductNum="",X_Type ="2"):
    url = url
    data = {"shopId":shopId,"personnelId":personnelId,"customerId":customerId,"cardType":cardType,"id":id,"deductNum":deductNum}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
# 3.4.8.6
def cardConsummerDetailList(url="",cardId="",pageSize="",X_Type="2"):
    url = url
    data = {"cardId":cardId,"pageSize":pageSize}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
# *********************************************3.5***********************************************
#3.5.1
def commentGroupNum(url ="",personnelId="",X_Type="2"):
    url = url
    data = {"personnelId":personnelId}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.5.2
def commentList(url="",personnelId="",commentLevel="",pageSize="",X_Type="2"):
    url = url
    data = {"personnelId":personnelId,"commentLevel":commentLevel,"pageSize":pageSize}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
# *********************************************3.6***********************************************
#3.6.1
def activityList(url="",shopId="",pageSiz="",X_Type="2"):
    url = url
    data = {"shopId":shopId,"pageSize":pageSiz}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.6.2
def activityDetail(url="",activityId="",shopId="",pageSize="",X_Type="2"):
    url = url
    data = {"activityId":activityId,"shopId":shopId,"pageSize":pageSize}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.6.3
def activityQr(url = "",shopId ="",activityId="",personnelId="",X_Type=""):
    url=url
    data = {"shopId":shopId,"activityId":activityId,"personnelId":personnelId}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#******************************************3.7************************************
#3.7.1
def createPlan(url ="",month= "",personnelId="",personnelPlanDetailDtos={},customerRankId="",planPerformance="",planIntroduce="",X_Type="2"):
    url = url
    data = {"month":month,"personnelId":personnelId,"personnelPlanDetailDtos":[{"customerRankId":customerRankId,"planPerformance":planPerformance,"planIntroduce":planIntroduce},]}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.7.2
def editPlan(url,id= "",personnelPlanDetailDtos={},customerRankId="",planPerformance="",planIntroduce="",X_Type="2"):
    url = url
    data = {"id":id,"personnelPlanDetailDtos":[{"customerRankId":customerRankId,"planPerformance":planPerformance,"planIntroduce":planIntroduce},]}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.7.3
def selectPlanDetail(url= "",planId="",X_Type="2"):
    url= url
    data = {"planId":planId}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.7.4
def selectCustomerList(url= "",shopId ="",personneId="",operationType="",recordType="",customerType="",X_Type ="2"):
    url = url
    data = {"shopId":shopId,"personnelId":personneId,"operationType":operationType,"recordType":recordType,"customerType":customerType}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.7.5
def selectPlanList(url ="",personnelId="",X_Type="2"):
    url = url
    data = {"personnelId":personnelId}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.7.6
def createDaySummarize(url="",personnelId="",day= "",dayPerformance="",dayExpend="",dayOrder= "",newExperienceIntroduce="",
                       newExperienceDevelop="",newTransactionIntroduce="",newTransactionDevelop="",summary="",performanceList={},
                       customerRankId="",planPerformance="",customerType="",expendList={},X_Type ="2"):
    url = url
    data = {"personnelId":personnelId,"day":day,"dayPerformance":dayPerformance,"dayExpend":dayExpend,"dayOrder":dayOrder,
            "newExperienceIntroduce":newExperienceIntroduce,"newExperienceDevelop":newExperienceDevelop,"newTransactionIntroduce":newTransactionIntroduce,
            "newTransactionDevelop":newTransactionDevelop,"summary":summary,
            "performanceList":[{"customerRankId":customerRankId,"planPerformance":planPerformance,"customerType":customerType}],
            "expendList":[{"customerRankId":customerRankId,"planPerformance":planPerformance,"customerType":customerType}]}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.7.7
def editDaySummarize(url="",planId="",id="",day= "",dayPerformance="",dayExpend="",dayOrder= "",newExperienceIntroduce="",
                       newExperienceDevelop="",newTransactionIntroduce="",newTransactionDevelop="",summary="",performanceList={},
                       customerRankId="",planPerformance="",customerType="",expendList={},X_Type ="2"):

    url = url
    data = {"planId": planId,"id":id, "day": day, "dayPerformance": dayPerformance, "dayExpend": dayExpend,
            "dayOrder": dayOrder,
            "newExperienceIntroduce": newExperienceIntroduce, "newExperienceDevelop": newExperienceDevelop,
            "newTransactionIntroduce": newTransactionIntroduce,
            "newTransactionDevelop": newTransactionDevelop, "summary": summary,
            "performanceList": [
                {"customerRankId": customerRankId, "planPerformance": planPerformance, "customerType": customerType}],
            "expendList": [
                {"customerRankId": customerRankId, "planPerformance": planPerformance, "customerType": customerType}]}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.7.8
def selectDaySummarizeDetail(url="",summarizeId="",X_Type="2"):
    url = url
    data = {"summarizeId":summarizeId}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.7.9
def selectSummarizeList(url="",planId="",X_Type="2"):
    url = url
    data = {"planId": planId}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)