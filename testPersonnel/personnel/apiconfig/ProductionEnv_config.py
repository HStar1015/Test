# -*- coding: utf-8 -*-
from ApiClass import *

APP_a = {
    "error_code_correct" :1,
    "error_code_fail":0,
    "phone":"15651966757",
    "password":"0adc3949ba59abbe56e057f20f883ee1",
    "authCode":"123456",#验证码
    "X-Type":2,
    "personnelId":17,#员工id
    "shopId":91,#员工对应门店id
    "businessId":15,#员工对应商家id
    "name":"xing",
    "sex":"1",#性别
    "provinceId":320000,#jiangsu
    "cityId":320500,#suzhou
    "areaId":320506,#wuzhongqu
    "registrationId":861759031496572,#EVL00
    "files":"",
    "monStart": "00:30",
    "monEnd": "21:00",
    "tueStart": "00:30",
    "tueEnd": "21:00",
    "wedStart": "00:30",
    "wedEnd": "21:00",
    "thuStart": "00:30",
    "thuEnd": "21:00",
    "friStart": "00:30",
    "friEnd": "21:00",
    "satStart": "00:30",
    "satEnd": "21:00",
    "sunStart": "00:30",
    "sunEnd": "21:00",
    "ifMonWork": 1,
    "ifTueWork": 1,
    "ifWedWork": 1,
    "ifThuWork": 1,
    "ifFriWork": 1,
    "ifSatWork": 1,
    "ifSunWork": 1,
    "pageSize":100,
    "projectId":"216",
    "orderNo":"DD7312548808254750113",#订单编号

}
Base_url = "https://www.iumer.cn/umer/webService"
Personnel_url = Base_url +"/personnel"

#************************3.1*******************************
#3.1.1注册
CoreServer_register_01 = register()
#input
CoreServer_register_01.url = Personnel_url +"/sys/user/register"
CoreServer_register_01.phone = APP_a["phone"]
CoreServer_register_01.password = APP_a["password"]
CoreServer_register_01.authCode = APP_a["authCode"]
CoreServer_register_01.inviteCode = "QWERTYU"
CoreServer_register_01.X_Type = APP_a["X-Type"]
#expect
CoreServer_register_01.code = APP_a["error_code_correct"]

#3.1.2登录
CoreServer_login_01 = login()
#input
CoreServer_login_01.url = Personnel_url + "/sys/user/login"
CoreServer_login_01.phone = APP_a["phone"]
CoreServer_login_01.password = APP_a["password"]
CoreServer_login_01.X_Type = APP_a["X-Type"]
#expect
CoreServer_login_01.code = APP_a["error_code_correct"]

#3.1.3
CoreServer_acceptInvitation_01 = acceptInvitation()
CoreServer_acceptInvitation_01.url = Personnel_url +"/sys/user/acceptInvitation"
CoreServer_acceptInvitation_01.X_Type = APP_a["X-Type"]
CoreServer_acceptInvitation_01.id = APP_a["personnelId"]
CoreServer_acceptInvitation_01.businessId = APP_a["businessId"]
CoreServer_acceptInvitation_01.shopId = APP_a["shopId"]
#exp
CoreServer_acceptInvitation_01.code = APP_a["error_code_correct"]

#3.1.4
CoreServer_personnelInfo_01 = personnelInfo()
CoreServer_personnelInfo_01.url = Personnel_url +"/sys/user/personnelInfo"
CoreServer_personnelInfo_01.X_Type = APP_a["X-Type"]
CoreServer_personnelInfo_01.id = APP_a["personnelId"]
#exp
CoreServer_personnelInfo_01.code = APP_a["error_code_correct"]
#3.1.5
CoreServer_updateInfo_01 = updateInfo()
CoreServer_updateInfo_01.url = Personnel_url +"/sys/user/updateInfo"
CoreServer_updateInfo_01.X_Type = APP_a["X-Type"]
CoreServer_updateInfo_01.id =APP_a["personnelId"]
CoreServer_updateInfo_01.name = APP_a["name"]
CoreServer_updateInfo_01.sex = APP_a["sex"]
CoreServer_updateInfo_01.files = APP_a["files"]
#Exp
CoreServer_updateInfo_01.code = APP_a["error_code_correct"]
#3.1.6
CoreServer_workTime = worlTime()
CoreServer_workTime.url = Personnel_url +"/sys/user/workTime"
CoreServer_workTime.id = APP_a["personnelId"]
CoreServer_workTime.monStart = APP_a["monStart"]
CoreServer_workTime.monEnd = APP_a["monEnd"]
CoreServer_workTime.tueStart = APP_a["tueStart"]
CoreServer_workTime.tueEnd = APP_a["tueEnd"]
CoreServer_workTime.wedStart = APP_a["wedStart"]
CoreServer_workTime.wedEnd = APP_a["wedEnd"]
CoreServer_workTime.thuStart =APP_a["thuStart"]
CoreServer_workTime.tueEnd = APP_a["tueEnd"]
CoreServer_workTime.friStart = APP_a["friStart"]
CoreServer_workTime.friEnd = APP_a["friEnd"]
CoreServer_workTime.ifMonWork = APP_a["ifMonWork"]
CoreServer_workTime.ifTueWork = APP_a["ifTueWork"]
CoreServer_workTime.ifThuWork = APP_a["ifThuWork"]
CoreServer_workTime.ifWedWork = APP_a["ifWedWork"]
CoreServer_workTime.ifFriWork = APP_a["ifFriWork"]
CoreServer_workTime.ifSatWork = APP_a["ifSatWork"]
CoreServer_workTime.ifSunWork = APP_a["ifSunWork"]
CoreServer_workTime.X_Type = APP_a["X-Type"]
#exp
CoreServer_workTime.code = APP_a["error_code_correct"]

#3.1.7
CoreServer_getWorkTime_01 = getWorkTime()
CoreServer_getWorkTime_01.url = Personnel_url +"/sys/user/getWorkTime"
CoreServer_getWorkTime_01.X_Type  = APP_a["X-Type"]
CoreServer_getWorkTime_01.personnelId = APP_a["personnelId"]
#exp
CoreServer_getWorkTime_01.code = APP_a["error_code_correct"]

#3.1.8
CoreServer_shopInfo_01 = shopInfo()
CoreServer_shopInfo_01.url = Personnel_url +"/sys/user/shopInfo"
CoreServer_shopInfo_01.X_Type = APP_a["X-Type"]
CoreServer_shopInfo_01.shopId = APP_a["shopId"]
#exp
CoreServer_shopInfo_01.code = APP_a["error_code_correct"]
#3.1.9
CoreServer_updateRegistrationId_01 = updateRegistrationId()
CoreServer_updateRegistrationId_01.url = Personnel_url + "/sys/user/updateRegistrationId"
CoreServer_updateRegistrationId_01.registrationId = APP_a["registrationId"]
#exp
CoreServer_updateRegistrationId_01.code = APP_a["error_code_correct"]
#***************************************3.2*******************************************
#3.2.1
CoreServer_projectList_01 = projectList()
CoreServer_projectList_01.url = Personnel_url + "/biz/project/projectList"
CoreServer_projectList_01.X_Type= APP_a["X-Type"]
CoreServer_projectList_01.shopId = APP_a["shopId"]
CoreServer_projectList_01.personnelId = APP_a["personnelId"]
CoreServer_projectList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_projectList_01.code = APP_a["error_code_correct"]
#3.2.2
CoreServer_chooseProject_01 = chooseProject()
CoreServer_chooseProject_01.url = Personnel_url +"/biz/project/chooseProject"
CoreServer_chooseProject_01.X_Type = APP_a["X-Type"]
CoreServer_chooseProject_01.personnelId = APP_a["personnelId"]
CoreServer_chooseProject_01.projectIds = APP_a["projectId"]
#exp
CoreServer_chooseProject_01.code = APP_a["error_code_correct"]
#3.2.3
CoreServer_myProjectList_01 = myProjectList()
CoreServer_myProjectList_01.url = Personnel_url +"/biz/project/myProjectList"
CoreServer_myProjectList_01.shopId = APP_a["shopId"]
CoreServer_myProjectList_01.personnelId = APP_a["personnelId"]
CoreServer_myProjectList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_myProjectList_01.code = APP_a["error_code_correct"]
#3.2.4
CoreServer_delProject_01 = delProject()
CoreServer_delProject_01.url = Personnel_url + "/biz/project/delProject"
CoreServer_delProject_01.X_Type = APP_a["X-Type"]
CoreServer_delProject_01.personnelId = APP_a["personnelId"]
CoreServer_delProject_01.projectIds = APP_a["projectId"]
#exp
CoreServer_delProject_01.code = APP_a["error_code_correct"]
#3.2.5
CoreServer_projectDetails_01 = projectDetails()
CoreServer_projectDetails_01.url = Personnel_url +"/biz/project/projectDetails"
CoreServer_projectDetails_01.X_Type = APP_a["X-Type"]
CoreServer_projectDetails_01.id = APP_a["projectId"]
#exp
CoreServer_projectDetails_01.code = APP_a["error_code_correct"]
#**************************************3.3*********************************************
#3.3.1
CoreServer_orderGroupNum_01 = orderGroupNum()
CoreServer_orderGroupNum_01.url = Personnel_url +"/biz/order/orderGroupNum"
CoreServer_orderGroupNum_01.X_Typze = APP_a["X-Type"]
CoreServer_orderGroupNum_01.shopId = APP_a["shopId"]
CoreServer_orderGroupNum_01.personnelId = APP_a["personnelId"]
#exp
CoreServer_orderGroupNum_01.code = APP_a["error_code_correct"]
#3.3.2
CoreServer_myOrderList_01= myOrderList()
CoreServer_myOrderList_01.url = Personnel_url +"/biz/order/myOrderList"
CoreServer_myOrderList_01.shopId = APP_a["shopId"]
CoreServer_myOrderList_01.personnelId = APP_a["personnelId"]
CoreServer_myOrderList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_myOrderList_01.code = APP_a["error_code_correct"]
#3.3.3
CoreServer_orderDetail_01 = orderDetail()
CoreServer_orderDetail_01.url = Personnel_url +"/biz/order/orderDetail"
CoreServer_orderDetail_01.X_Type = APP_a["X-Type"]
CoreServer_orderDetail_01.personnelId  =APP_a["personnelId"]
CoreServer_orderDetail_01.orderNo = APP_a["orderNo"]
#exp
CoreServer_orderDetail_01.code= APP_a["error_code_correct"]