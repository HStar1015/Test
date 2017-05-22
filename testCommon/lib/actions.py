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

#5.1
def authPhone(url ="",type="",phone="",operationType =""):
    url = url
    data1 = {"type":type,"phone":phone,"operationType":operationType}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"type":type,"phone":phone,"operationType":operationType,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
    return null2None2dict(res)

#5.2
def authPic(url= "",phone= ""):
    url =url
    data1 = {"phone": phone}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"phone": phone,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
    return res
#5.3
def projectTypeTree(url=""):
    url = url
    data1 = {}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
    return res
#5.4
def messages(url="",banner="",platform ="",pageSize=""):
    url = url
    data1 = {"banner":banner,"platform":platform,"pageSize":pageSize}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"banner":banner,"platform":platform,"pageSize":pageSize,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
    return res
#5.5
def rankList(url=""):
    url = url
    data1 = {}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
    return res
#5.6
def getShareUrl(url="",type="",id=""):
    url = url
    data1 = {"type":type,"id":id}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"type":type,"id":id,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
    return res
#5.7
def findPassword(url="",authCode="",type="",phone="",newPassword=""):
    url = url
    data1 = {"authCode":authCode,"type":type,"phone":phone,"newPassword":newPassword}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"authCode":authCode,"type":type,"phone":phone,"newPassword":newPassword,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
    return res
#5.8
def updatePassword(url="",type="",phone="",oldPassword="",newPassword=""):
    url = url
    data1 = {"type":type,"phone":phone,"oldPassword":oldPassword,"newPassword":newPassword}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"type":type,"phone":phone,"oldPassword":oldPassword,"newPassword":newPassword,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
    return res
#5.9
def payMode(url ="",type=""):
    url = url
    data1 = {"type":type}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"type":type,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
    return res
#5.10
def areaList(url="",cityId =""):
    url = url
    data1 = {"cityId":cityId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"cityId":cityId,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
    return res
#5.11
def activityDetail(url= "",id= "",userId ="",type=""):
    url = url
    data1 = {"id":id,"userId":userId,"type":type}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"id":id,"userId":userId,"type":type,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
    return res
#5.12
def vote(url = "",activityId = "",contentId = "",phone= ""):
    url = url
    data1 = {"activityId":activityId,"contentId":contentId,"phone":phone}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"activityId":activityId,"contentId":contentId,"phone":phone,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
    return res
#5.13
def voteStatical(url = "",activityId = ""):
    url = url
    data1 = {"activityId":activityId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"activityId":activityId,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
    return res
#5.14
def winList(url = "",activityId = ""):
    url = url
    data1 = {"activityId":activityId}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"activityId":activityId,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
    return res
#5.15
def peopleVoteStatus(url = "",activityId = "",phone=""):
    url = url
    data1 = {"activityId":activityId,"phone":phone}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"activityId":activityId,"phone":phone,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
    return res
#5.16
def projectPhoto(url="",groupNo =""):
    url = url
    data1 = {"groupNo":groupNo}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"groupNo":groupNo, "sign": sign}
    token =mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return res
#5.17
def baiduCoordinate(url="",latitude ="",longitude=""):
    url = url
    data1 = {"latitude":latitude,"longitude":longitude}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"latitude":latitude,"longitude":longitude, "sign": sign}
    token =mylogin()
    header = {"Content-type": "application/json;charset=UTF-8", "X-Type": 1, "X-Token": token['data']['token']}
    res = post_json(url, data, header)
    return res
#5.18
def getOpenId(url="",jsCode=""):
    url = url
    data1 = {"jsCode":jsCode}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"jsCode":jsCode, "sign": sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
    return res
#5.19
def reservePeriodList(url =""):
    url = url
    data1 = {}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
    return res
#5.20
def reserveTimeList(url="",personnelId= "",dateTime= ""):
    url = url
    data1 = {"personnelId":personnelId,"dateTime":dateTime}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"personnelId":personnelId,"dateTime":dateTime,"sign":sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
    return res
#5.21
def feedback(url= "",userType= "",userId="",phone= "",name="",content=""):
    url = url
    data1 = {"userType": userType, "userId": userId,"phone":phone,"name":name,"content":content}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"userType": userType, "userId": userId,"phone":phone,"name":name,"content":content, "sign": sign}
    token = mylogin()
    header = {"Content-type": "application/json;charset=UTF-8","X-Type":1,"X-Token":token['data']['token']}
    res = post_json(url, data, header)
    return res
#5.22
def getShareQR(url="",personnelId= "",path= "",width =""):
    url = url
    data1 = {"personnelId":personnelId,"path":path,"width":width}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res1 = res.replace("%3A%2F%2F","://")
    res11 = res1.replace("%2F","/")
    res111 = res11.replace("%3F","?")
    res1111 = res111.replace("%3D","=")
    res11111 = res1111.replace("%26","&")
    res111111 = res11111.replace("%23","#")
    res2 = res111111 + key
    sign = md5(res2).upper()
    data = {"personnelId":personnelId,"path":path,"width":width, "sign": sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
    return res
#5.23
def versionRenewal(url="",os ="",port=""):
    url = url
    data1 = {"os":os,"port":port}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res+ key
    sign = md5(res2).upper()
    data = {"os":os,"port":port,"sign": sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
#5.24
def getZoning(url=""):
    url = url
    data1 = {}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"sign": sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
#5.25
def getCitySort(url =""):
    url = url
    data1 = {}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"sign": sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)
#5.26
def getBankCardList(url =""):
    url = url
    data1 = {}
    sort_data = sorted(data1.items(), key=lambda d: d[0])
    res = urllib.urlencode(sort_data)
    res2 = res + key
    sign = md5(res2).upper()
    data = {"sign": sign}
    header = {"Content-type": "application/json;charset=UTF-8"}
    res = post_json(url, data, header)