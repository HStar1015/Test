# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import simplejson as json
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import types
import hashlib
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


def mylogin():
    # 登录用如下这个接口
    url_login = 'https://www.iumer.cn/umer/webService/customer/sys/user/login'

    # 自定义请求头
    header_login = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3"}

    # 访问登录页面
    data_login = {'phone': '15651966757', 'password': '0adc3949ba59abbe56e057f20f883ee1',
                  "sign": "E3599E79A9ABB6EED2DED4481090C716"}
    res = post_json(url_login, data_login, header_login)

    return null2None2dict(res)
#******************************************4.1*************************************************
#4.1.1
def register(url = "",phone="",password= "",authCode ="",X_Type="3"):
    url = url
    data1 ={"phone":phone,"password":password,"authCode":authCode}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data ={"phone":phone,"password":password,"authCode":authCode,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8","X-Type":"3"}
    res = post_json(url,data,header)
    return null2None2dict(res)
#4.1.2
def login(url="",phone ="",password="",X_Type="3"):
    url = url
    data1 = {"phone":phone,"password":password}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"phone":phone,"password":password,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8","X-Type":"3"}
    res = post_json(url,data,header)
    return null2None2dict(res)
#!!!!!4.1.3
def updateInfo(url = "",id ="",files="",X_Type="3"):
    url = url
    data = files
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8","X-Type":"3","X-Token":token['data']['token'],"id":id}
    header.update(header)
    res  = post_upload_file(url,data,header)
    return null2None2dict(res)
#4.1.4
def customerInfo(url ="",id ="",X_Type="3"):
    url = url
    data1 = {"id":id}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"id": id,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8","X-Type":"3","X-Token":token['data']['token']}
    res = post_json(url,data,header)
    return  null2None2dict(res)
#4.1.5
def collectProject(url="",customerId="",projectId="",ifCollect="",X_Type="3"):
    url = url
    data1 = {"customerId":customerId,"projectId":projectId,"ifCollect":ifCollect}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"customerId":customerId,"projectId":projectId,"ifCollect":ifCollect,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.1.6
def collectProjectList(url="",customerId="",longitude="",latitude="",pageSize= "",X_Type="3"):
    url = url
    data1 = {"customerId":customerId,"longitude":longitude,"latitude":latitude,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"customerId":customerId,"longitude":longitude,"latitude":latitude,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.1.7
def collectPersonnel(url ="",customerId="",personnelId="",ifCollect="",X_Type="3"):
    url = url
    data1 = {"customerId":customerId,"personnelId":personnelId,"ifCollect":ifCollect}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"customerId":customerId,"personnelId":personnelId,"ifCollect":ifCollect,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.1.8
def collectPersonnelList(url="",customerId="",longitude="",latitude="",pageSize= "",X_Type="3"):
    url = url
    data1 = {"customerId":customerId,"longitude":longitude,"latitude":latitude,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"customerId":customerId,"longitude":longitude,"latitude":latitude,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
# #4.1.9
# def miniAppLogin(url = "",openId="",X_Type="3"):
#     url = url
#     data1 = {"openId":openId}
#     sort_data = sorted(data1.items(), key=lambda d: d[0])
#     res = urllib.urlencode(sort_data)
#     res2 = res + key
#     sign = md5(res2).upper()
#     data = {"openId":openId,"sign":sign}
#     token = mylogin()
#     header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
#     res = post_json(url, data, header)
#     return null2None2dict(res)
#****************************************4.2*********************************
#4.2.1
def projectPersonnelList(url = "",projectId="",pageSize="",X_Type="3"):
    url = url
    data1 = {"projectId":projectId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"projectId":projectId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.2.2
def personnelProjectList(url = "",personnelId="",pageSize="",X_Type="3"):
    url = url
    data1 = {"personnelId":personnelId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"personnelId":personnelId,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.2.3
def orderSave(url = "",projectId="",personnelId="",customerId="",makeStartDate="",makeEndDate="",priceType="",reserveName="",reservePhone="",X_Type="3"):
    url = url
    data1 = {"personelId":personnelId,"projectId":projectId,"personnelId":personnelId,"customerId":customerId,"makeStartDate":makeStartDate,
             "makeEndDate":makeEndDate,"priceType":priceType,"reserveName":reserveName,"reservePhone":reservePhone}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"personnelId":personnelId,"projectId":projectId,"personnelId":personnelId,"customerId":customerId,"makeStartDate":makeStartDate,
             "makeEndDate":makeEndDate,"priceType":priceType,"reserveName":reserveName,"reservePhone":reservePhone,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.2.4
def cancelOrder(url="",orderNo="",customerId="",X_Type="3"):
    url = url
    data1 = {"orderNo":orderNo,"customerId":customerId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"orderNo":orderNo,"customerId":customerId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.2.5
def applyCancelOrder(url="",orderNo="",customerId="",X_Type="3"):
    url = url
    data1 = {"orderNo":orderNo,"customerId":customerId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"orderNo":orderNo,"customerId":customerId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.2.6
def personnelServeProject(url="",projectId="",personnelId="",X_Type="3"):
    url = url
    data1 = {"projectId":projectId,"personnelId":personnelId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"projectId":projectId,"personnelId":personnelId,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#******************************************************4.3******************************************************
#4.3.1.1
def hotProject(url="",longitude="",latitude="",cityId ="",pageSize="",X_Type="3"):
    url = url
    data1 = {"longitude":longitude,"latitude":latitude,"cityId":cityId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"longitude": longitude, "latitude": latitude, "cityId": cityId, "pageSize": pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.3.1.2
def searchProjectList(url = "",cityId= "",longitude="",latitude ="",page ="",pageSize="",X_Type ="3"):
    url = url
    data1 = {"cityId":cityId,"longitude":longitude,"latitude":latitude,"page":page,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"cityId":cityId,"longitude":longitude,"latitude":latitude,"page":page,"pageSize":pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.3.1.3
def projectDetails(url ="",id ="",X_Type ="3"):
    url = url
    data1 = {"id":id}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"id":id,"sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.3.1.4
def projectCommentGroupNum(url ="",projectId ="",X_Type ="3"):
    url = url
    data1 = {"projectId":projectId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"projectId":projectId,"sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.3.1.5
def projectCommentList(url ="",projectId="",commentLevel="",pageSize="3"):
    url = url
    data1 = {"projectId":projectId,"commentLevel":commentLevel,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    print "res2 = ",res2
    sign = md5(res2).upper()
    data = {"projectId": projectId, "commentLevel": commentLevel, "pageSize": pageSize,"sign":sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)

#4.3.2.1
def hotPersonnel(url ="",longitude="",latitude ="",cityId ="",pageSize ="",X_Type ="3"):
    url = url
    data1 = {"longitude":longitude,"latitude":latitude,"cityId":cityId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    print "res2 = ", res2
    sign = md5(res2).upper()
    data = {"longitude": longitude, "latitude": latitude, "cityId": cityId, "pageSize": pageSize,"sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.3.2.2
def searchPersonnelList(url ="",cityId ="",longitude="",latitude ="",pageSize ="",X_Type ="3"):
    url = url
    data1 = {"cityId":cityId,"longitude":longitude,"latitude":latitude,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    print "res2 = ", res2
    sign = md5(res2).upper()
    data = {"cityId": cityId,"longitude": longitude, "latitude": latitude,  "pageSize": pageSize,"sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.3.2.3
def personnelDetail(url ="",id="",X_Type="3"):
    url = url
    data1 = {"id":id}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    print "res2 = ", res2
    sign = md5(res2).upper()
    data = {"id": id,"sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.3.3.4
def personnelProjectList(url ="",shopId="",personnelId ="",pageSize ="",X_Type="3"):
    url = url
    data1 = {"shopId":shopId,"personnelId":personnelId,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"shopId":shopId,"personnelId":personnelId,"pageSize":pageSize, "sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.3.3.5
def personnelCommentGroupNum (url ="",personnelId="",X_Type="3"):
    url = url
    data1 = {"personnelId":personnelId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"personnelId":personnelId,"sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.3.3.6
def personnelCommentList(url ="",personnelId="",commentLevel="",pageSize="",X_Type="3"):
    url = url
    data1= {"personnelId":personnelId,"commentLevel":commentLevel,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"personnelId":personnelId,"commentLevel":commentLevel,"pageSize":pageSize,"sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#***********************************************4.4******************************************************
#4.4.1
def reserveProjectRecord(url ="",customerId="",longitude="",latitude="",pageSize="",X_Type="3"):
    url = url
    data1 = {"customerId":customerId,"longitude":longitude,"latitude":latitude,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    print "res2 = ",res2
    sign = md5(res2).upper()
    data = {"customerId":customerId,"longitude":longitude,"latitude":latitude,"pageSize":pageSize,"sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.4.2
def reservePersonnelRecord(url ="",customerId="",longitude="",latitude="",pageSize="",X_Type="3"):
    url = url
    data1 = {"customerId":customerId,"longitude":longitude,"latitude":latitude,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    print "res2 = ",res2
    sign = md5(res2).upper()
    data = {"customerId":customerId,"longitude":longitude,"latitude":latitude,"pageSize":pageSize,"sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.4.3
def orderGroupNum(url ="",customerId ="",X_Type ="3"):
    url = url
    data1= {"customerId":customerId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    print "res2 = ", res2
    sign = md5(res2).upper()
    data = {"customerId": customerId,"sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.4.4
def myOrderList(url ="",customerId ="",approveStatus ="",pageSize ="",X_Type="3"):
    url = url
    data1 = {"customerId":customerId,"approveStatus":approveStatus,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    print "res2 = ", res2
    sign = md5(res2).upper()
    data = {"customerId":customerId,"approveStatus":approveStatus,"pageSize":pageSize, "sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.4.5
def orderDetail(url ="",customerId ="",orderNo ="",X_Type="3"):
    url = url
    data1 = {"customerId":customerId,"orderNo":orderNo}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    print "res2 = ", res2
    sign = md5(res2).upper()
    data = {"customerId":customerId,"orderNo":orderNo, "sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.4.6
def payQRDetail(url ="",customerId ="",orderNo ="",X_Type="3"):
    url = url
    data1 = {"customerId":customerId,"orderNo":orderNo}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    print "res2 = ", res2
    sign = md5(res2).upper()
    data = {"customerId":customerId,"orderNo":orderNo, "sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.4.7
def orderComment (url ="",orderNo="",customerId ="",personnelId="",projectId="",content="",domainLevel="",serveLevel="",communicationLevel="",X_Type="3"):
    url = url
    data1 = {"orderNo":orderNo,"customerId":customerId,"personnelId":personnelId,"projectId":projectId,"content":content,"domainLevel":domainLevel,
             "serveLevel":serveLevel,"communicationLevel":communicationLevel}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    print "res2 = ", res2
    sign = md5(res2).upper()
    data = {"orderNo":orderNo,"customerId":customerId,"personnelId":personnelId,"projectId":projectId,"content":content,"domainLevel":domainLevel,
             "serveLevel":serveLevel,"communicationLevel":communicationLevel, "sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.4.8
def confirmFinishOrder(url ="",personnelId ="",orderNo ="",X_Type ="3"):
    url = url
    data1 = {"personnelId":personnelId,"orderNo": orderNo}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    print "res2 = ", res2
    sign = md5(res2).upper()
    data = {"personnelId":personnelId,"orderNo": orderNo, "sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.4.8
def wechatSubmitPay(url ="",openId ="",customerId="",orderNo ="",paymentMode ="",X_Type ="3"):
    url = url
    data1 = {"openId":openId,"customerId":customerId,"orderNo":orderNo,"paymentMode":paymentMode}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    print "res2 = ", res2
    sign = md5(res2).upper()
    data = {"openId":openId,"customerId":customerId,"orderNo":orderNo,"paymentMode":paymentMode, "sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.4.8
def appSubmitPay(url ="",customerId="",orderNo ="",paymentMode ="",X_Type ="3"):
    url = url
    data1 = {"customerId":customerId,"orderNo":orderNo,"paymentMode":paymentMode}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    print "res2 = ", res2
    sign = md5(res2).upper()
    data = {"customerId":customerId,"orderNo":orderNo,"paymentMode":paymentMode, "sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)
#4.4.8
def checkOrderPayStatus(url ="",customerId="",orderNo ="",X_Type ="3"):
    url = url
    data1 = {"customerId":customerId,"orderNo":orderNo}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    print "res2 = ", res2
    sign = md5(res2).upper()
    data = {"customerId":customerId,"orderNo":orderNo, "sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": "3", "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return null2None2dict(res)

