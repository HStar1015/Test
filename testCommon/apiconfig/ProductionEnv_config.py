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
}
Base_url = "https://www.iumer.cn/umer/webService"
Common_url = Base_url +"/common"

#5.1
CoreServer_authPhone_01 = authPhone()
CoreServer_authPhone_01.url = Common_url + "/authPhone"
CoreServer_authPhone_01.type  = 1

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
