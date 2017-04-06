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
