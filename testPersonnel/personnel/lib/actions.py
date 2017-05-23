# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import simplejson as json
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import types
import hashlib
import mimetools
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

def encode_multipart_formdata(key, value):
    bundary = mimetools.choose_boundary()
    BOUNDARY = '----------'+bundary+'--'

    CRLF = '\r\n'

    L = []

    L.append('--' + BOUNDARY)

    L.append('Content-Disposition: form-data; name="%s"' % key)

    L.append('')

    L.append(value)

    L.append('--' + BOUNDARY + '--')

    L.append('')

    body = CRLF.join(L)

    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY

    return content_type, body

def post_multipart(url, fields):
    content_type, body = encode_multipart_formdata("data",fields)

    req = urllib2.Request(url, body)

    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 SE 2.X MetaSr 1.0)")

    req.add_header("Accept", "*/*")

    req.add_header("Accept-Language", "zh-CN,zh;q=0.8")

    req.add_header("Accept-Encoding", "gzip,deflate,sdch")

    req.add_header("Connection", "keep-alive")

    req.add_header("Content-Type", content_type)

    req.add_header("User-Agent1", "SogouMSE")

    req.add_header('X-Type',3)

    token = mylogin()['data']['token']

    req.add_header("X-Token",token)


    req_header_get = req.header_items()
    print "***request header_get = ***\n%s" % req_header_get

    req_body = req.get_data()
    print "***request body = ***\n%s" % req_body

    res = urllib2.urlopen(req)
    res_code = res.getcode()
    print "***response code = ***\n%s" % res_code

    try:
        response = urllib2.urlopen(req)
        the_page = response.read().decode('utf-8')
        print the_page
        return the_page
    except urllib2.HTTPError, e:
        print e.code
        pass
    except urllib2.URLError, e:
        print str(e)
        pass

#************************************************************************************
def mylogin():
    # 登录用如下这个接口
    url_login = 'https://www.iumer.cn/umer/webService/personnel/sys/user/login'

    # 自定义请求头
    header_login ={"Content-type": "application/json;charset=UTF-8","X-Type":"2"}

    # 访问登录页面
    data_login = {'phone':'15651966757', 'password':'0adc3949ba59abbe56e057f20f883ee1',"sign":"E3599E79A9ABB6EED2DED4481090C716"}
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
    data1 ={"phone":phone,"password":password,"authCode":authCode}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data ={"phone":phone,"password":password,"authCode":authCode,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8","X-Type":"2"}
    res = post_json(url,data,header)
    return null2None2dict(res)
#3.1.2
def login(url="",phone ="",password="",X_Type="2"):
    url = url
    data1= {"phone":phone,"password":password}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"phone":phone,"password":password,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8","X-Type":"2"}
    res = post_json(url,data,header)
    return null2None2dict(res)
#3.1.3
def acceptInvitation(url = "",id ="",businessId="",X_Type="2"):
    url = url
    data1 = {"id":id,"businessId":businessId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"id":id,"businessId":businessId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2","X-Token":token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.1.4
def personnelInfo(url ="",id= "",X_Type = "2"):
    url = url
    data1  = {"id":id}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data  = {"id":id,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.1.5
def updateInfo(url= "",id = "",name="",sex="",X_Type="2",files=""):
    url = url
    data1 = {"id":id,"name":name,"sex":sex}
    sort_data = sorted(data1.items(),key=lambda d:d[0])
    res = urllib.unquote(urllib.urlencode(sort_data))
    res2 = res + key
    sign = md5(res2).upper()
    data = {"id":id,"name":name,"sex":sex,"sign":sign}
    data2 = json.dumps(data)
    res = post_multipart(url,data2)
    return  null2None2dict(res)
#3.1.6
def workTime(url = "",id = "", monStart ="",monEnd="",tueStart="",tueEnd="",wedStart="",
    wedEnd="",thuStart="",thuEnd="",friStart="",friEnd="",satStart="",satEnd="",sunStart="",sunEnd="",
    ifMonWork="",ifTueWork="",ifWedWork="",ifThuWork="",ifFriWork="",ifSatWork="",ifSunWork="",X_Type="2"):
    url = url
    data1 = {"monStart":monStart,"monEnd":monEnd,"tueStart":tueStart,"tueEnd":tueEnd,
            "wedStart":wedStart,"wedEnd":wedEnd,"thuStart":thuStart,"thuEnd":tueEnd,"friStart":friStart,"friEnd":friEnd,
            "satStart":satStart,"satEnd":satEnd,"sunStart":sunStart,"sunEnd":sunEnd,"ifMonWork":ifMonWork,"ifTueWork":ifTueWork,"ifWedWork":ifWedWork,
            "ifThuWork":ifThuWork,"ifFriWork":ifFriWork,"ifSatWork":ifSatWork,"ifSunWork":ifSunWork}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.unquote(urllib.urlencode(sort_data))
    res2 = res + key
    sign = md5(res2).upper()
    data = {"monStart": monStart, "monEnd": monEnd, "tueStart": tueStart, "tueEnd": tueEnd,
            "wedStart": wedStart, "wedEnd": wedEnd, "thuStart": thuStart, "thuEnd": tueEnd, "friStart": friStart,
            "friEnd": friEnd,
            "satStart": satStart, "satEnd": satEnd, "sunStart": sunStart, "sunEnd": sunEnd, "ifMonWork": ifMonWork,
            "ifTueWork": ifTueWork, "ifWedWork": ifWedWork,
            "ifThuWork": ifThuWork, "ifFriWork": ifFriWork, "ifSatWork": ifSatWork, "ifSunWork": ifSunWork,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.1.7
def getWorkTime(url ="",personnelId ="",X_Type="2"):
    url = url
    data1 = {"personnelId":personnelId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"personnelId":personnelId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.1.8
def shopInfo(url = "",shopId= "",X_Type = "2"):
    url = url
    data1 = {"shopId":shopId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.1.9
def updateRegistrationId(url = "",id="",registrationId="",X_Type="2"):
    url = url
    data1 = {"id":id,"registrationId":registrationId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"id":id,"registrationId":registrationId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#**********************************3.2*****************************************
#3.2.1
def projecList(url = "",shopId ="",personnelId="",pageSize="",X_Type="2"):
    url = url
    data1 = {"shopId":shopId,"personnelId":personnelId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"personnelId":personnelId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.2.2
def chooseProject(url ="",projectIds ="",personnelId="",X_Type = "2"):
    url = url
    data1 = {"projectIds":projectIds,"personnelId":personnelId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"projectIds":projectIds,"personnelId":personnelId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.2.3
def myProjectList(url = "",shopId= "",personnelId="",pageSize="",X_Type =""):
    url = url
    data1 = {"shopId":shopId,"personnelId":personnelId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"personnelId":personnelId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.2.4
def delProject(url = "",projectIds ="",personnelId="",X_Type= "2"):
    url = url
    data1 = {"projectIds":projectIds,"personnelId":personnelId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"projectIds":projectIds,"personnelId":personnelId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.2.5
def projectDetails(url ="",id ="",X_Type =""):
    url = url
    data1 = {"id":id}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"id":id,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#***********************************3.3************************************
#3.3.1
def orderGroupNum(url = "",shopId ="",personnelId="",X_Typ ="2"):
    url = url
    data1 = {"shopId":shopId,"personnelId":personnelId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"personnelId":personnelId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.3.2
def myOrderList(url ="",shopId= "",personnelId="",pageSize= "",X_Type ="2"):
    url = url
    data1 = {"shopId": shopId, "personnelId": personnelId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId": shopId, "personnelId": personnelId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.3.3
def orderDetail(url="",personnelId="",orderNo="",X_Type= ""):
    url = url
    data1= {"personnelId":personnelId,"orderNo":orderNo}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data= {"personnelId":personnelId,"orderNo":orderNo,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.3.4
def cancelOrder(url ="",personnelId="",orderNo="",X_Type="2"):
    url = url
    data1 = {"personnelId":personnelId,"orderNo":orderNo}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"personnelId":personnelId,"orderNo":orderNo,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.3.5
def confirmFinishOrder(url = "",personnelId="",orderNo="",X_Type="2"):
    url = url
    data1 = {"personnelId": personnelId, "orderNo": orderNo}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"personnelId": personnelId, "orderNo": orderNo,"sign":sign}

    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.3.6
def scanFinishOrder(url = "",personnelId="",payCode="",X_Type="2"):
    url = url
    data1 = {"personnelId": personnelId, "payCode":payCode}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"personnelId": personnelId, "payCode":payCode,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.3.7
def orderSave(url ="",projectId = "",personnelId = "",makeStartDate="",makeEndDate="",priceType="",reserveName="",
              reservePhone="",X_Type = "2"):
    url = url;
    data1 ={"projectId":projectId,"personnelId":personnelId,"makeStartDate":makeStartDate,"makeEndDate":makeEndDate,
           "priceType": priceType, "reserveName": reserveName, "reservePhone": reservePhone}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.unquote(urllib.urlencode(sort_data))
    res1 = res.replace("+"," ")
    res2 = res1 + key
    sign = md5(res2).upper()
    data = {"projectId": projectId, "personnelId": personnelId, "makeStartDate": makeStartDate,
            "makeEndDate": makeEndDate,
            "priceType": priceType, "reserveName": reserveName, "reservePhone": reservePhone,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#***********************************************3.4************************************************
#3.4.1
def customerList(url ="",shopId = "",personnelId="",pageSize="",X_Type=""):
    url = url
    data1= {"shopId":shopId,"personnelId":personnelId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data= {"shopId":shopId,"personnelId":personnelId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.4.2
def changeRemark(url="",shopId="",personnelId="",remark="",customerId="",X_Type=""):
    url = url
    data1 = {"shopId":shopId,'personnelId':personnelId,"remark":remark,"customerId":customerId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,'personnelId':personnelId,"remark":remark,"customerId":customerId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.4.3
def changeRank(url = "",shopId = "",rankId ="",customerIds="",X_Type ="2"):
    url = url
    data1= {"shopId":shopId,"rankId":rankId,"customerIds":customerIds}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"rankId":rankId,"customerIds":customerIds,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.4.4
def customerDetails(url ="",shopId = "",customerId ="",X_Type="2"):
    url = url
    data1 = {"shopId":shopId,"customerId":customerId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"customerId":customerId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.4.5
def expenseRecord(url ="",customerId ="",shopId ="",pageSize ="",X_Type="2"):
    url = url
    data1 = {"customerId":customerId,"shopId":shopId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"customerId":customerId,"shopId":shopId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.4.6
def expenseProject(url="",customerId ="",shopId= "",pageSize="",X_Type ="2"):
    url = url
    data1 = {"customerId":customerId,"shopId":shopId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"customerId":customerId,"shopId":shopId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.4.7
def rankInfoList(url ="",shopId="",personnelId ="",X_Type ="2"):
    url = url
    data1 = {"shopId":shopId,"personnelId":personnelId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"personnelId":personnelId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#!3.4.8.1
def createCard(url="",shopId="",personnelId="",customerId="",cardType="",name="",remark="",validityDate="",X_Type="2"):
    url = url
    data1 = {"shopId":shopId,"personnelId":personnelId,"customerId":customerId,"cardType":cardType,
            "name":name,"remark":remark,"validityDate":validityDate}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.unquote(urllib.urlencode(sort_data))
    print"BBBBBBBBBBBBBBBBBBB",res
    res1 =res.replace("+"," ")
    res2 = res1 + key
    print "RRRRRRRRRRRRRRRRRRRRRRR",res2
    sign = md5(res2).upper()
    data = {"shopId": shopId, "personnelId": personnelId, "customerId": customerId, "cardType": cardType,
             "name": name, "remark": remark, "validityDate": validityDate,"sign":sign}
    token = mylogin()

    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
# 3.4.8.2
def editCard(url="",shopId="",personnelId="",customerId="",cardType="",id="",name="",remark="",validityDate="",X_Type="2"):
    url = url
    data1 = {"shopId":shopId,"personnelId":personnelId,"customerId":customerId,"cardType":cardType,"id":id,
            "name":name,"remark":remark,"validityDate":validityDate}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.unquote(urllib.urlencode(sort_data))
    print"BBBBBBBBBBBBBBBBBBB",res
    res1 =res.replace("+"," ")
    res2 = res1 + key
    print "RRRRRRRRRRRRRRRRRRRRRRR",res2
    sign = md5(res2).upper()
    data = {"shopId": shopId, "personnelId": personnelId, "customerId": customerId, "cardType": cardType, "id": id,
            "name": name, "remark": remark, "validityDate": validityDate,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
# 3.4.8.3
def cardDetail(url="",cardId="",X_Type="2"):
    url = url
    data1 = {"cardId":cardId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"cardId":cardId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
# 3.4.8.4
def customerCardList(url="",shopId="",customerId="",pageSize="",page="",X_Type = "2"):
    url = url
    data1 ={"shopId":shopId,"customerId":customerId,"pageSize":pageSize,"page":page}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data ={"shopId":shopId,"customerId":customerId,"pageSize":pageSize,"page":page,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
# 3.4.8.5
def operationCard(url="",shopId = "",personnelId="",customerId="",cardType="",id ="",deductNum="",X_Type ="2"):
    url = url
    data1 = {"shopId":shopId,"personnelId":personnelId,"customerId":customerId,"cardType":cardType,"id":id,"deductNum":deductNum}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"personnelId":personnelId,"customerId":customerId,"cardType":cardType,"id":id,"deductNum":deductNum,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
# 3.4.8.6
def cardConsummerDetailList(url="",cardId="",pageSize="",X_Type="2"):
    url = url
    data1 = {"cardId":cardId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"cardId":cardId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
# *********************************************3.5***********************************************
#3.5.1
def commentGroupNum(url ="",personnelId="",X_Type="2"):
    url = url
    data1 = {"personnelId":personnelId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"personnelId":personnelId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.5.2
def commentList(url="",personnelId="",commentLevel="",pageSize="",X_Type="2"):
    url = url
    data1 = {"personnelId":personnelId,"commentLevel":commentLevel,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"personnelId":personnelId,"commentLevel":commentLevel,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
# *********************************************3.6***********************************************
#3.6.1
def activityList(url="",shopId="",pageSiz="",X_Type="2"):
    url = url
    data1 = {"shopId":shopId,"pageSize":pageSiz}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"pageSize":pageSiz,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.6.2
def activityDetail(url="",activityId="",shopId="",pageSize="",X_Type="2"):
    url = url
    data1 = {"activityId":activityId,"shopId":shopId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"activityId":activityId,"shopId":shopId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.6.3
def activityQr(url = "",shopId ="",activityId="",personnelId="",X_Type=""):
    url=url
    data1 = {"shopId":shopId,"activityId":activityId,"personnelId":personnelId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"activityId":activityId,"personnelId":personnelId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#******************************************3.7************************************
#!!!!!!!!!!!!!!3.7.1
def createPlan(url ="",month= "",personnelId="",personnelPlanDetailDtos={},customerRankId="",planPerformance="",planIntroduce="",X_Type="2"):
    url = url
    data1 = {"month":month,"personnelId":personnelId,"personnelPlanDetailDtos":[{"customerRankId":customerRankId,"planPerformance":planPerformance,"planIntroduce":planIntroduce},]}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.unquote(urllib.urlencode(sort_data))
    res2 = res + key
    sign = md5(res2).upper()
    data = {"month":month,"personnelId":personnelId,"personnelPlanDetailDtos":[{"customerRankId":customerRankId,"planPerformance":planPerformance,"planIntroduce":planIntroduce},],"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.7.2
def editPlan(url,id= "",personnelPlanDetailDtos={},customerRankId="",planPerformance="",planIntroduce="",X_Type="2"):
    url = url
    data1 = {"id":id,"personnelPlanDetailDtos":[{"customerRankId":customerRankId,"planPerformance":planPerformance,"planIntroduce":planIntroduce},]}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    print"BBBBBBBBBBBBBBBBBBBBBBB" ,res2

    sign = md5(res2).upper()
    data = {"id":id,"personnelPlanDetailDtos":[{"customerRankId":customerRankId,"planPerformance":planPerformance,"planIntroduce":planIntroduce},],"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.7.3
def selectPlanDetail(url= "",planId="",X_Type="2"):
    url= url
    data1 = {"planId":planId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"planId":planId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.7.4
def selectCustomerList(url= "",shopId ="",personneId="",operationType="",recordType="",customerType="",X_Type ="2"):
    url = url
    data1 = {"shopId":shopId,"personnelId":personneId,"operationType":operationType,"recordType":recordType,"customerType":customerType}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"personnelId":personneId,"operationType":operationType,"recordType":recordType,"customerType":customerType,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.7.5
def selectPlanList(url ="",personnelId="",X_Type="2"):
    url = url
    data1 = {"personnelId":personnelId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"personnelId":personnelId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.7.6
def createDaySummarize(url="",personnelId="",day= "",dayPerformance="",dayExpend="",dayOrder= "",newExperienceIntroduce="",
                       newExperienceDevelop="",newTransactionIntroduce="",newTransactionDevelop="",summary="",performanceList={},
                       customerRankId="",planPerformance="",customerType="",expendList={},X_Type ="2"):
    url = url
    data1 = {"personnelId":personnelId,"day":day,"dayPerformance":dayPerformance,"dayExpend":dayExpend,"dayOrder":dayOrder,
            "newExperienceIntroduce":newExperienceIntroduce,"newExperienceDevelop":newExperienceDevelop,"newTransactionIntroduce":newTransactionIntroduce,
            "newTransactionDevelop":newTransactionDevelop,"summary":summary,
            "performanceList":[{"customerRankId":customerRankId,"planPerformance":planPerformance,"customerType":customerType}],
            "expendList":[{"customerRankId":customerRankId,"planPerformance":planPerformance,"customerType":customerType}]}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"personnelId": personnelId, "day": day, "dayPerformance": dayPerformance, "dayExpend": dayExpend,
            "dayOrder": dayOrder,
            "newExperienceIntroduce": newExperienceIntroduce, "newExperienceDevelop": newExperienceDevelop,
            "newTransactionIntroduce": newTransactionIntroduce,
            "newTransactionDevelop": newTransactionDevelop, "summary": summary,
            "performanceList": [
                {"customerRankId": customerRankId, "planPerformance": planPerformance, "customerType": customerType}],
            "expendList": [
                {"customerRankId": customerRankId, "planPerformance": planPerformance, "customerType": customerType}],
            "sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.7.7
def editDaySummarize(url="",planId="",id="",day= "",dayPerformance="",dayExpend="",dayOrder= "",newExperienceIntroduce="",
                       newExperienceDevelop="",newTransactionIntroduce="",newTransactionDevelop="",summary="",performanceList={},
                       customerRankId="",planPerformance="",customerType="",expendList={},X_Type ="2"):

    url = url
    data1 = {"planId": planId,"id":id, "day": day, "dayPerformance": dayPerformance, "dayExpend": dayExpend,
            "dayOrder": dayOrder,
            "newExperienceIntroduce": newExperienceIntroduce, "newExperienceDevelop": newExperienceDevelop,
            "newTransactionIntroduce": newTransactionIntroduce,
            "newTransactionDevelop": newTransactionDevelop, "summary": summary,
            "performanceList": [
                {"customerRankId": customerRankId, "planPerformance": planPerformance, "customerType": customerType}],
            "expendList": [
                {"customerRankId": customerRankId, "planPerformance": planPerformance, "customerType": customerType}]}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"planId": planId, "id": id, "day": day, "dayPerformance": dayPerformance, "dayExpend": dayExpend,
            "dayOrder": dayOrder,
            "newExperienceIntroduce": newExperienceIntroduce, "newExperienceDevelop": newExperienceDevelop,
            "newTransactionIntroduce": newTransactionIntroduce,
            "newTransactionDevelop": newTransactionDevelop, "summary": summary,
            "performanceList": [
                {"customerRankId": customerRankId, "planPerformance": planPerformance, "customerType": customerType}],
            "expendList": [
                {"customerRankId": customerRankId, "planPerformance": planPerformance, "customerType": customerType}],
            "sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.7.8
def selectDaySummarizeDetail(url="",summarizeId="",X_Type="2"):
    url = url
    data1 = {"summarizeId":summarizeId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"summarizeId":summarizeId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#3.7.9
def selectSummarizeList(url="",planId="",X_Type="2"):
    url = url
    data1 = {"planId": planId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"planId": planId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "2", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)