# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import simplejson as json
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import hashlib
import types
key="&key=037F6F3127604B4FAE8AAD1AE4BE78E3"
#MD5加密
def md5(str):
    if type(str) is types.StringType:
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
        print """""", m.hexdigest
    else:
        return "ErrorType!"

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
    data =urllib.urlencode(data)

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
    res_body = res.read()

    print "***response body = ***\n%s" % res_body
    res.close()

    return res_body
#************************************************************************************
def mylogin():
    # 登录用如下这个接口
    url_login = 'https://www.iumer.cn/umer/webService/shop/sys/business/login'

    # 自定义请求头
    header_login ={"Content-type": "application/json;charset=UTF-8","X-Type":"1"}

    # 访问登录页面
    data_login = {'phone':'15651966757', 'password':'0adc3949ba59abbe56e057f20f883ee1',"sign":"E3599E79A9ABB6EED2DED4481090C716"}
    res = post_json(url_login,data_login, header_login)

    return null2None2dict(res)

def null2None2dict(res=""):
    res = res.replace("null", "None")
    res = res.replace("false", "False")
    res = res.replace("true", "True")
    return eval(res)
#******************************************2.1*************************************************
#注册
def register_test(url = "",phone="",password= "",authCode ="",inviteCode="",X_Type="1"):
    url = url
    data1 = {"phone": phone, "password": password, "authCode": authCode, "inviteCode": inviteCode}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data ={"phone":phone,"password":password,"authCode":authCode,"inviteCode":inviteCode,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8","X-Type":"1"}
    res = post_json(url,data,header)
    return null2None2dict(res)
#登录
def login_test(url="",phone ="",password="",X_Type="1"):
    url = url
    data = {"phone":phone,"password":password,"sign":"E3599E79A9ABB6EED2DED4481090C716"}
    header = {"Content-type": "application/json;charset=UTF-8","X-Type":"1"}
    res = post_json(url,data,header)
    return null2None2dict(res)
#申请邀请码
def applyInvite_test(url="",phone ="",name="",pronvinceId="",cityId ="",areaId = "",X_Type="1"):
    url = url
    data1 = {"phone":phone,"name":name,"provinceId":pronvinceId,"cityId":cityId,"areaId":areaId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"phone":phone,"name":name,"provinceId":pronvinceId,"cityId":cityId,"areaId":areaId,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "1"}
    res = post_json(url, data, header)
    return null2None2dict(res)
#!!!!!!!!!!!!!!!!修改商家信息
def updateInfo_test(url="",id="",files="",X_Type = '1'):
    url = url
    data1 = {"id":id}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data= {"id":id,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "1","X-Token":token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#获取商家信息
def businessInfo_test(url="",id="",X_Type = '1'):
    url = url
    data1 = {"id":id}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"id": id,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1,"X-Token":token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#更新用户设备ID
def updateRegistrationId(url ="",id ="",registrationId="",X_Type = '1'):
    url = url
    data1 = {"id": id, "registrationId": registrationId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"id": id,"registrationId":registrationId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#************************2.2*******************************
#!!!!!!!!!!!!!!!!2.2.1
def saveShop(url ="",businessId="",phone="",shopName= "",shortName= "",description= "",provinceId="",cityId="",areaId="",address="",X_Type="1",files=""):

    data = files
    token = mylogin()
    header = {"Content-type": "application/octet-stream", "X-Type": 1, "X-Token": token['data']['token'],"businessId":businessId,"phone":phone,"shopName":shopName,"shortName":shortName,"description":description,"provinceId":provinceId,
            "cityId":cityId,"areaId":areaId,"address":address}
    header.update(header)
    res = post_upload_file(url, data, header)
    return null2None2dict(res)
#!!!!!!!!!!!!!!!!!2.2.2
def updateInfo(url ="",businessId="",phone="",shopName= "",shortName= "",description= "",provinceId="",cityId="",areaId="",address="",X_Type="1",files=""):

    data = files
    token = mylogin()
    header = {"Content-type": "application/octet-stream", "X-Type": 1, "X-Token": token['data']['token'],"businessId":businessId,"phone":phone,"shopName":shopName,"shortName":shortName,"description":description,"provinceId":provinceId,
            "cityId":cityId,"areaId":areaId,"address":address}
    header.update(header)
    res = post_upload_file(url, data, header)
    return null2None2dict(res)
#2.2.3
def shopList(url="",businessId="",X_Type='1'):
    url = url
    data1 = {"businessId": businessId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"businessId": businessId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.2.4
def shopInfo(url ="",id ="",X_Type ='1'):
    url = url
    data1 = {"id":id}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"id":id,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url ,data,header)
    return null2None2dict(res)
#2.2.5
def deleteShop(url ="",businessId= "",id ="",X_Type='1'):
    url = url
    data1 = {"id":id,"businessId":businessId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"id":id,"businessId":businessId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.2.6.1
def shopStatics(url="",shopId="",X_Type="1"):
    url =url
    data1 = {"shopId":shopId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.2.6.2
def saleStatics(url="",shopId="",X_Type="1"):
    url =url
    data1 = {"shopId":shopId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.2.6.3
def newCustomerStatistics(url="",shopId="",X_Type="1"):
    url =url
    data1 = {"shopId":shopId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.2.6.3
def projectSaleStatistics(url="",shopId="",X_Type="1"):
    url =url
    data1 = {"shopId":shopId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#************************2.3*******************************
#!!!!!!!!!!!!!!!!2.3.1
def addProject(url = "",businessId="",shopIds ="",projectName="",groupNo="",unitPrice="",coursePrice= "",courseRemark="",
               duration ="",description= "",applyPerson ="",brand="",noticeMatters="",X_Type="1",files =""):
    url = url
    file = files
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token'],
            "businessId":businessId,"shopIds":shopIds,"projectName":projectName,"groupNo":groupNo,"unitPrice":unitPrice,"coursePrice":coursePrice,
              "courseRemark":courseRemark,"duration":duration,"description":description,"applyPerson":applyPerson,"brand":brand,
              "noticeMatters":noticeMatters,"files":files}
    res = post_upload_file(url,file,header)
    return null2None2dict(res)
#2.3.2
def deleteProject(url ="",id="",X_Type ="1"):
    url = url
    data1 = {"id":id}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"id":id,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url,data,header)
    return null2None2dict(res)
#!!!!!!!!!2.3.3
def editProject(url="", id="", projectName="", groupNo="", unitPrice="", coursePrice="",
                courseRemark="",duration="", description="", applyPerson="", brand="", noticeMatters="",
               X_Type="1", files="",fileUuid =""):
    url = url
    file = files
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token'],
          "id": id,  "projectName": projectName, "groupNo": groupNo,
          "unitPrice": unitPrice, "coursePrice": coursePrice,
          "courseRemark": courseRemark, "duration": duration, "description": description, "applyPerson": applyPerson,
          "brand": brand,  "noticeMatters": noticeMatters, "files": files,"fileUuid":fileUuid}
    res = post_upload_file(url,file,header)
    return null2None2dict(res)
#2.3.4
def projectList(url="",shopId="",pageSize="",X_Type="1"):
    url = url
    data1 = {"shopId":shopId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header= {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url,data,header)
    return null2None2dict(res)
#2.3.5
def projectDetails(url="",id ="",X_Type ="1"):
    url = url
    data1= {"id":id}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data= {"id":id,"sign":sign}
    token = mylogin()
    header= {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url ,data ,header)
    return null2None2dict(res)
#2.3.6
def copyProject(url ="",businessId="",shopId="",projectIds ="",X_Type= "1"):
    url= url
    data1 ={"businessId":businessId,"shopId":shopId,"projectIds":projectIds}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data ={"businessId":businessId,"shopId":shopId,"projectIds":projectIds,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url,data,header)
    return null2None2dict(res)

#***************************************2.4.1************************************
#2.4.1
def pushIncvitation(url ="",personnelPhone="",businessId="",shopId ="",phone="",X_Type="1"):
    url = url
    data1 = {"personnelPhone":personnelPhone,"businessId":businessId,"shopId":shopId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"personnelPhone":personnelPhone,"businessId":businessId,"shopId":shopId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url,data,header )
    return  null2None2dict(res)
#2.4.2
def personnelList(url ="",businessId="",pageSize="",X_Type="1"):
    url = url
    data1 = {"businessId":businessId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"businessId":businessId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.4.3
def personnelDetails(url= "",id ="",X_Type = "1"):
    url = url
    data1 = {"id":id}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"id":id,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.4.4
def unbind(url="",id="",businessId="",X_Type='1'):
    url = url
    data1 ={"id":id,"businessId":businessId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data ={"id":id,"businessId":businessId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url,data,header)
    return  null2None2dict(res)
#2.4.5
def allocationPersonnel(url="",businessId="",shopId="",personnelIds="" ,X_Type='1'):
    url = url
    data1={"businessId":businessId,"shopId":shopId,"personnelIds":personnelIds}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data={"businessId":businessId,"shopId":shopId,"personnelIds":personnelIds,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url,data,header)
    return  null2None2dict(res)
#2.4.6.1
def commentGroupNum(url="",personnelId="",X_Type = "1"):
    url = url
    data1 = {"personnelId":personnelId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"personnelId":personnelId,"sign":sign}
    token = mylogin()
    header ={"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url,data,header)
    return null2None2dict(res)
#2.4.6.2
def commentList(url="",personnelId="",commentLevel="",pageSize="",X_Type = "1"):
    url = url
    data1 ={"personnelId":personnelId,"commentLevel":commentLevel,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data ={"personnelId":personnelId,"commentLevel":commentLevel,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.4.7.1
def daySummarizeList(url="",day="",shopId="",pageSize="",X_Type ="1"):
    url = url
    data1 = {"day":day,"shopId":shopId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"day":day,"shopId":shopId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.4.7.2
def daySummarizeDetail(url="",summarizeId = "",X_Type="1"):
    url = url
    data1 = {"summarizeId":summarizeId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"summarizeId":summarizeId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.4.7.3
def monthPlanList(url="",month="",shopId="",pageSize="",X_Type=""):
    url = url
    data1 = {"month":month,"shopId":shopId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"month":month,"shopId":shopId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.4.7.4
def monthPlanDetail(url="",planId="",X_Type=""):
    url = url
    data1 = {"planId":planId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"planId":planId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.4.8.1
def operationCaseList(url="",shopId ="",X_Type ="1"):
    url = url
    data1 = {"shopId": shopId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId": shopId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.4.8.2
def operationCaseDetail(url="",shopId="",month="",X_Type=""):
    url = url
    data1 = {"shopId": shopId,"month":month}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId": shopId,"month":month,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#************************2.5*******************************
#2.5.1
def customerList(url ="",shopId="",pageSize="",X_Type="1"):
    url = url
    data1 = {"shopId":shopId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.5.2
def customerDetails(url ="",shopId= "",customerId="",X_Type= "1"):
    url= url
    data1={"shopId":shopId,"customerId":customerId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data={"shopId":shopId,"customerId":customerId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.5.3
def allocationCustomer(url="",shopId="",personnelId="",customerId="",X_Type="1"):
    url = url
    data1 = {"shopId":shopId,"personnelId":personnelId,"customerId":customerId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"personnelId":personnelId,"customerId":customerId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.5.4
def expenseRecord(url ="",customerId="",shopId="",pageSize ="",X_Type="1"):
    url = url
    data1 ={"customerId":customerId,"shopId":shopId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data ={"customerId":customerId,"shopId":shopId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.5.5
def expenseProject(url ="",customerId="",shopId="",pageSize ="",X_Type="1"):
    url = url
    data1 ={"customerId":customerId,"shopId":shopId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data ={"customerId":customerId,"shopId":shopId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.5.6
def changeRank(url="",shopId ="",rankId="",customerIds="",X_Type="1"):
    url = url
    data1 = {"shopId":shopId,"rankId":rankId,"customerId":customerIds}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"rankId":rankId,"customerId":customerIds,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.5.7
def rankInfoList(url = "",shopId="",X_Type="1"):
    url = url
    data1 = {"shopId":shopId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.5.8.1
def customerCardList(url="",shopId ="",customerId="",pageSize="",X_Type="1"):
    url = url
    data1 = {"shopId":shopId,"customerId":customerId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"customerId":customerId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.5.8.2
def cardConsummerDetailList(url ="",cardId="",pageSize="",X_Type="1"):
    url = url
    data1 = {"cardId": cardId, "pageSize": pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"cardId": cardId, "pageSize": pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#*****************************************2.6*****************************************
#2.6.1
def findAccountBalance(url="",businessId="",X_Type =""):
    url = url
    data1= {"businessId":businessId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data= {"businessId":businessId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.6.2
def accountRecordList(url ="",businessId="",pageSize="",X_Type =""):
    url = url
    data1= {"businessId":businessId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data= {"businessId":businessId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.6.3
def putApply(url= "",businessId= "",paymentMode="",price="",X_Type ="1"):
    url = url
    data1 = {"businessId":businessId,"paymentMode":paymentMode,"price":price}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"businessId":businessId,"paymentMode":paymentMode,"price":price,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.6.4
def putRecordDetails(url ="",id = "",X_Type= "1"):
    url = url
    data1 = {"id":id}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"id":id,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.6.5
def incomeRecordDetail(url = "",id="",X_Type="1"):
    url= url
    data1 = {"id": id}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"id": id,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#**********************************************2.7*****************************************
#2.7.1
def shopCapacity(url = "",businessId= "",shopId="",bunkCount="",projectAverageDuration ="",workStartDate = "", workEndDate = "",personnelCount = ""
    ,customerAverageExpense = "",activeCustomerCount = "",mainProjectAverageDuration = "",X_Type=""):
    url = url
    data1= {"businessId":businessId,"shopId":shopId,"bunkCount":bunkCount,"projectAverageDuration":projectAverageDuration,
           "workStartDate":workStartDate,"workEndDate":workEndDate,"personnelCount":personnelCount,
           "customerAverageExpense":customerAverageExpense,"activeCustomerCount":activeCustomerCount,"mainProjectAverageDuration":mainProjectAverageDuration}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"businessId": businessId, "shopId": shopId, "bunkCount": bunkCount,
            "projectAverageDuration": projectAverageDuration,
            "workStartDate": workStartDate, "workEndDate": workEndDate, "personnelCount": personnelCount,
            "customerAverageExpense": customerAverageExpense, "activeCustomerCount": activeCustomerCount,
            "mainProjectAverageDuration": mainProjectAverageDuration,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.7.2
def shopDiagnose(url="",businessId ="",shopId="",monthShopTurnover="",dayShopCustomerCount="",personnelCount="",monthTookeenCount="",
                 yearShopTurnover=""):
    url = url
    data1 = {"businessId":businessId,"shopId":shopId,"monthShopTurnover":monthShopTurnover,"dayShopCustomerCount":dayShopCustomerCount,
            "personnelCount":personnelCount,"monthTookeenCount":monthTookeenCount,"yearShopTurnover":yearShopTurnover}

    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"businessId": businessId, "shopId": shopId, "monthShopTurnover": monthShopTurnover,
            "dayShopCustomerCount": dayShopCustomerCount,
            "personnelCount": personnelCount, "monthTookeenCount": monthTookeenCount,
            "yearShopTurnover": yearShopTurnover,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.7.3
def getShopCapacity(url ="",businessId ="",shopId ="",X_Type="1"):
    url = url
    data1 = {"businessId":businessId,"shopId":shopId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"businessId":businessId,"shopId":shopId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.7.4
def getShopDiagnose(url ="",businessId ="",shopId ="",X_Type="1"):
    url = url
    data1 = {"businessId":businessId,"shopId":shopId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"businessId":businessId,"shopId":shopId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#**************************************2.8********************************************
#2.8.1
def createActivity(url="",businessId = "",shopId="",activityName="",activityStartDate="",
                   activityEndDate="",activityUnitPrice="",
                   activityCoursePrice="",description="",projectIds="",X_Type="1"):
    url=url
    data1 ={"businessId": businessId,"shopId": shopId,"activityName": activityName,"activityStartDate": activityStartDate,"activityEndDate": activityEndDate,
        "activityUnitPrice": activityUnitPrice,"activityCoursePrice": activityCoursePrice,"projectIds": projectIds}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"businessId": businessId, "shopId": shopId, "activityName": activityName,
            "activityStartDate": activityStartDate, "activityEndDate": activityEndDate,
            "activityUnitPrice": activityUnitPrice, "activityCoursePrice": activityCoursePrice,
            "projectIds": projectIds,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.8.2
def activityList(url="",shopId="",pageSize ="",X_Type =""):
    url = url
    data1 = {"shopId":shopId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.8.3
def activiDetail(url = "",activityId ="",shopId ="",pageSize = "",X_Type ="1"):
    url = url
    data1 = {"activityId":activityId,"shopId":shopId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"activityId":activityId,"shopId":shopId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.8.4
def activityQr(url = "",shopId="",activityId="",X_Type="1"):
    url = url
    data1 = {"shopId":shopId,"activityId":activityId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"activityId":activityId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.8.5
def activityPersonnelList(url="",activityId="",pageSize= "",X_Type="1"):
    url = url
    data1 = {"activityId":activityId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"activityId":activityId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#2.8.6
def activityChooseProjectList(url ="",shopId = "",pageSize="",X_Type="1"):
    url = url
    data1 = {"shopId":shopId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)