# -*- coding: utf-8 -*-
from ApiClass import *

APP_a = {
    "error_code_correct" :1,
    "error_code_fail":0,
    "phone":"15651966757",
    "password":"0adc3949ba59abbe56e057f20f883ee1",
    "authCode":"123456",#验证码
    "X-Type":1,
    "operationType":2,
    "banner":"index",
    "platform":"shop",
    "pageSize":100,
    "type":1,
    "id":38,#分享URl-id
    "cityId":"371000",
    "userId":"180",
    "activityId":"26",
    "contentId":"45",
    "groupNo":"1002",
    "longitude": "120.635753",
    "latitude": "31.267955",
    "jsCode":"1234",
    "personnelId":"177",
    "dataTime":"2017-05-26",
    "name":"Tester",
    "content":"Test",
    "path":"https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxfa398cdc57b80304&redirect_uri=https://www.iumer.cn/umer/wechat/index/shopDetail?shopId=38&urlType=share&response_type=code&scope=snsapi_userinfo&state=STATE&connect_redirect=1#wechat_redirect",
    "width":"100",
    "os_android":"android",
    "os_ios":"ios",
    "port_0":0,
    "port_1":1,
}
Base_url = "https://www.iumer.cn/umer/webService"
Common_url = Base_url +"/common"

#5.1
CoreServer_authPhone_01 = authPhone()
CoreServer_authPhone_01.url = Common_url + "/authPhone"
CoreServer_authPhone_01.type  =APP_a["type"]

CoreServer_authPhone_01.phone = APP_a["phone"]
CoreServer_authPhone_01.operationType = APP_a["operationType"]
#exp
CoreServer_authPhone_01.code = APP_a["error_code_correct"]

#5.2
CoreServer_authPic_01 = authPic()
CoreServer_authPic_01.url = Common_url +"/authPic"
CoreServer_authPic_01.phone = APP_a["phone"]
#exp
CoreServer_authPic_01.code  = APP_a["error_code_correct"]

#5.3
CoreServer_projectTypeTree_01 = projectTypeTree()
CoreServer_projectTypeTree_01.url = Common_url +"/projectTypeTree"
#exp
CoreServer_projectTypeTree_01.code = APP_a["error_code_correct"]

#5.4
CoreServer_message_01 = message()
CoreServer_message_01.url = Common_url +"/messages"
CoreServer_message_01.banner = APP_a["banner"]
CoreServer_message_01.platform = APP_a["platform"]
CoreServer_message_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_message_01.code = APP_a["error_code_correct"]

#5.5
CoreServer_rankList_01 = rankList()
CoreServer_rankList_01.url = Common_url + "/rankList"
#exp
CoreServer_rankList_01.code = APP_a["error_code_correct"]

#5.6
CoreServer_getShareUrl_01 = getShareUrl()
CoreServer_getShareUrl_01.url = Common_url + "/getShareUrl"
CoreServer_getShareUrl_01.type = APP_a["type"]
CoreServer_getShareUrl_01.id = APP_a["id"]
#exp
CoreServer_getShareUrl_01.code = APP_a["error_code_correct"]

#5.7
CoreServer_findPassword_01 = findPassword()
CoreServer_findPassword_01.url = Common_url+ "/findPassword"
CoreServer_findPassword_01.authCode = APP_a["authCode"]
CoreServer_findPassword_01.type =APP_a["type"]
CoreServer_findPassword_01.phone = APP_a["phone"]
CoreServer_findPassword_01.newPassword = APP_a["password"]
#exp
CoreServer_findPassword_01.code = APP_a["error_code_correct"]

#5.8
CoreServer_updatePassword_01 = updatePassword()
CoreServer_updatePassword_01.url = Common_url+ "/findPassword"
CoreServer_updatePassword_01.oldPassword = APP_a["password"]
CoreServer_updatePassword_01.type =APP_a["type"]
CoreServer_updatePassword_01.phone = APP_a["phone"]
CoreServer_updatePassword_01.newPassword = APP_a["password"]
#exp
CoreServer_findPassword_01.code = APP_a["error_code_correct"]

#5.9
CoreServer_payMode_01 = payMode()
CoreServer_payMode_01.url = Common_url + "/payMode"
CoreServer_payMode_01.type = APP_a["type"]
#exp
CoreServer_payMode_01.code = APP_a["error_code_correct"]

#5.10
CoreServer_areaList_01 = areaList()
CoreServer_areaList_01.url = Common_url + "/areaList"
CoreServer_areaList_01.cityId = APP_a["cityId"]
#exp
CoreServer_areaList_01.code = APP_a["error_code_correct"]

#5.11
CoreServer_activityDetail_01 = activityDetail()
CoreServer_activityDetail_01.url = Common_url + "/activityDetail"
CoreServer_activityDetail_01.id = APP_a["activityId"]
CoreServer_activityDetail_01.userId = APP_a["userId"]
CoreServer_activityDetail_01.type = APP_a["X-Type"]
#exp
CoreServer_activityDetail_01.code = APP_a["error_code_correct"]

#5.12
CoreServer_vote_01 = vote()
CoreServer_vote_01.url  = Common_url + "/vote"
CoreServer_vote_01.activityId = APP_a["activityId"]
CoreServer_vote_01.contentId = APP_a["contentId"]
CoreServer_vote_01.phone = APP_a["phone"]
#exp
CoreServer_vote_01.code = APP_a["error_code_correct"]

#5.13
CoreServer_voteStatical_01 = voteStatical()
CoreServer_voteStatical_01.url = Common_url + "/voteStatistical"
CoreServer_voteStatical_01.activityId = APP_a["activityId"]
#exp
CoreServer_voteStatical_01.code = APP_a["error_code_correct"]

#5.14
CoreServer_winList_01 = winList()
CoreServer_winList_01.url = Common_url + "/winList"
CoreServer_winList_01.activityId = APP_a["activityId"]
#exp
CoreServer_winList_01.code = APP_a["error_code_correct"]

#5.15
CoreServer_peopleVoteStatus_01 = peopleVoteStatus()
CoreServer_peopleVoteStatus_01.url = Common_url + "/peopleVoteStatus"
CoreServer_peopleVoteStatus_01.activityId = APP_a["activityId"]
CoreServer_peopleVoteStatus_01.phone = APP_a["phone"]
#exp
CoreServer_peopleVoteStatus_01.code  = APP_a["error_code_correct"]

#5.16
CoreServer_projectPhoto_01 = projectPhoto()
CoreServer_projectPhoto_01.url = Common_url  + "/projectPhoto"
CoreServer_projectPhoto_01.groupNo = APP_a["groupNo"]
#exp
CoreServer_projectPhoto_01.code  = APP_a["error_code_correct"]

#5.17
CoreServer_baiduCoordinate_01 = baiduCoordinate()
CoreServer_baiduCoordinate_01.url = Common_url + "/baiduCoordinate"
CoreServer_baiduCoordinate_01.latitude = APP_a["latitude"]
CoreServer_baiduCoordinate_01.longitude = APP_a["longitude"]
#exp
CoreServer_baiduCoordinate_01.code = APP_a["error_code_correct"]

#5.18
CoreServer_getOpenId_01 = getOpenId()
CoreServer_getOpenId_01.url = Common_url + "/getOpenId"
CoreServer_getOpenId_01.jsCode = APP_a["jsCode"]
#exp
CoreServer_getOpenId_01.code = APP_a["error_code_correct"]

#5.19
CoreServer_reservePeriodList_01 = reservePeriodList()
CoreServer_reservePeriodList_01.url = Common_url +"/reservePeriodList"
#exp
CoreServer_reservePeriodList_01.code = APP_a["error_code_correct"]

#5.20
CoreServer_reserveTimeList_01 = reserveTimeList()
CoreServer_reserveTimeList_01.url = Common_url + "/reserveTimeList"
CoreServer_reserveTimeList_01.dateTime = APP_a["dataTime"]
CoreServer_reserveTimeList_01.personnelId = APP_a["personnelId"]
#exp
CoreServer_reserveTimeList_01.code = APP_a["error_code_correct"]

#5.21
CoreServer_feedback_01  = feedback()
CoreServer_feedback_01.url = Common_url + "/feedback"
CoreServer_feedback_01.userType = APP_a["X-Type"]
CoreServer_feedback_01.userId = APP_a["userId"]
CoreServer_feedback_01.phone = APP_a["phone"]
CoreServer_feedback_01.name = APP_a["name"]
CoreServer_feedback_01.content = APP_a["content"]
#exo
CoreServer_feedback_01.code = APP_a["error_code_correct"]

#5.22
CoreServer_getShareQR_01 = getShareUrl()
CoreServer_getShareQR_01.url = Common_url + "/getShareQR"
CoreServer_getShareQR_01.personnelId = APP_a["personnelId"]
CoreServer_getShareQR_01.path = APP_a["path"]
CoreServer_getShareQR_01.width = APP_a["width"]
#exp
CoreServer_getShareQR_01.code = APP_a["error_code_correct"]

#5.23
CoreServer_versionRenewal_01 = versionRenewal()
CoreServer_versionRenewal_01.url = Common_url + "/version/versionRenewal"
CoreServer_versionRenewal_01.os = APP_a["os_android"]
CoreServer_versionRenewal_01.port = APP_a["port_0"]
#exp
CoreServer_versionRenewal_01.code = APP_a["error_code_correct"]

#5.24
CoreServer_getZoning_01 = getZonig()
CoreServer_getZoning_01.url = Common_url + "/getZoning"
#exp
CoreServer_getZoning_01.code = APP_a["error_code_correct"]

#5.25
CoreServer_getCitySort_01 = getCtiySort()
CoreServer_getCitySort_01.url = Common_url + "/getCitySort"
#exp
CoreServer_getZoning_01.code = APP_a["error_code_correct"]

#5.26
CoreServer_getBankCardList_01 = getBankCardList()
CoreServer_getBankCardList_01.url = Common_url + "/getBankCardList"
#exp
CoreServer_getBankCardList_01.code = APP_a["error_code_correct"]