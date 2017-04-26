# -*- coding: utf-8 -*-
from ApiClass import *

APP_a = {
    "error_code_correct" :1,
    "error_code_fail":0,
    "phone":"15651966757",
    "password":"0adc3949ba59abbe56e057f20f883ee1",
    "authCode":"123456",#验证码
    "X-Type":3,
    "personnelId":17,#员工id
    "shopId":91,#员工对应门店id
    "businessId":15,#员工对应商家id
    "name":"xing",
    "sex":"1",#性别
    "provinceId":320000,#jiangsu
    "cityId":320500,#suzhou
    "areaId":320506,#wuzhongqu
    "registrationId":861759031496572,#EVL00
    "ifCollect":1,
    "files":"",
    "pageSize":100,
    "projectId":"216",
    "orderNo":"DD7312548808254750113",#订单编号
    "payCode":"QR7543166741178590773",#支付码
    "makeStartDate":"2017-05-28 12:00:00",#预约开始时间
    "makeEndDate":"2017-03-25 12:30:00",#预约结束时间
    "priceType":1,#价格类型,0(单价)/1(疗程)
    "reserveName":"xing",
    "reservePhone":"13051175683",
    "customerId":43,#顾客id
    "remark":"hello",
    "rankId":1,
    "activityId":163,
    "longitude":"120.635753",
    "latitude":"31.267955",
    "openId":"oV4G3v3Na7WiI6hP7JEbZgXqAi2I",
    "reserveName":"hanxing",
    "reservePhone":"13013013012",
    "orderNo":"DD4692409678014280"

}
Base_url = "https://www.iumer.cn/umer/webService"
Customer_url = Base_url +"/customer"

#************************3.1*******************************
#4.1.1注册
CoreServer_register_01 = register()
#input
CoreServer_register_01.url = Customer_url +"/sys/user/register"
CoreServer_register_01.phone = APP_a["phone"]
CoreServer_register_01.password = APP_a["password"]
CoreServer_register_01.authCode = APP_a["authCode"]
CoreServer_register_01.inviteCode = "123456"
CoreServer_register_01.X_Type = APP_a["X-Type"]
#expect
CoreServer_register_01.code = APP_a["error_code_correct"]

#4.1.2登录
CoreServer_login_01 = login()
#input
CoreServer_login_01.url = Customer_url + "/sys/user/login"
CoreServer_login_01.phone = APP_a["phone"]
CoreServer_login_01.password = APP_a["password"]
CoreServer_login_01.X_Type = APP_a["X-Type"]
#expect
CoreServer_login_01.code = APP_a["error_code_correct"]

#4.1.3
CoreServer_updateInfo_01 = updateInfo()
CoreServer_updateInfo_01.url = Customer_url +"/sys/user/updateInfo"
CoreServer_updateInfo_01.X_Type = APP_a["X-Type"]
CoreServer_updateInfo_01.id = APP_a["customerId"]
CoreServer_updateInfo_01.files = APP_a["files"]
#exp
CoreServer_updateInfo_01.code = APP_a["error_code_correct"]
#4.1.4
CoreServer_customerInfo_01 = cutomerInfo()
CoreServer_customerInfo_01.X_Type = APP_a["X-Type"]
CoreServer_customerInfo_01.url = Customer_url +"/sys/user/customerInfo"
CoreServer_customerInfo_01.id = APP_a["customerId"]
#exp
CoreServer_customerInfo_01.code = APP_a["error_code_correct"]
#4.1.5
CoreServer_collectProject_01 = collectProject()
CoreServer_collectProject_01.url = Customer_url + "/sys/user/collectProject"
CoreServer_collectProject_01.X_Type = APP_a["X-Type"]
CoreServer_collectProject_01.customerId = APP_a["customerId"]
CoreServer_collectProject_01.projectId = APP_a["projectId"]
CoreServer_collectProject_01.ifCollect = APP_a["ifCollect"]
#exp
CoreServer_collectProject_01.code = APP_a["error_code_correct"]
#4.1.6
CoreServer_collectProjectList_01 = collectProjectList()
CoreServer_collectProjectList_01.url = Customer_url +"/sys/user/collectProjectList"
CoreServer_collectProjectList_01.X_Type = APP_a["X-Type"]
CoreServer_collectProjectList_01.longitude = APP_a["longitude"]
CoreServer_collectProjectList_01.latitude = APP_a["latitude"]
CoreServer_collectProjectList_01.pageSize = APP_a["pageSize"]
CoreServer_collectProjectList_01.customerId = APP_a["customerId"]
#exp
CoreServer_collectProjectList_01.code = APP_a["error_code_correct"]
#4.1.7
CoreServer_collectPersonnel_01 = collectPersonnel()
CoreServer_collectPersonnel_01.url = Customer_url +"/sys/user/collectPersonnel"
CoreServer_collectPersonnel_01.X_Type = APP_a["X-Type"]
CoreServer_collectPersonnel_01.customerId = APP_a["customerId"]
CoreServer_collectPersonnel_01.personnelId = APP_a["personnelId"]
CoreServer_collectPersonnel_01.ifCollect = APP_a["ifCollect"]
#exo
CoreServer_collectPersonnel_01.code = APP_a["error_code_correct"]
#4.1.8
CoreServer_collectPersonnelList_01 = collectPersonnelList()
CoreServer_collectPersonnelList_01.url = Customer_url +"/sys/user/collectProjectList"
CoreServer_collectPersonnelList_01.X_Type = APP_a["X-Type"]
CoreServer_collectPersonnelList_01.longitude = APP_a["longitude"]
CoreServer_collectPersonnelList_01.latitude = APP_a["latitude"]
CoreServer_collectPersonnelList_01.pageSize = APP_a["pageSize"]
CoreServer_collectPersonnelList_01.customerId = APP_a["customerId"]
#4.1.9
CoreServer_miniAppLogin_01 = miniAppLogin()
CoreServer_miniAppLogin_01.url = Customer_url + "/sys/user/miniAppLogin"
CoreServer_miniAppLogin_01.X_Type = APP_a["X-Type"]
CoreServer_miniAppLogin_01.openId = APP_a["openId"]
#exp
CoreServer_miniAppLogin_01.code = APP_a["error_code_correct"]
#***************************************4.2******************************************
#4.2.1
CoreServer_projectPersonnelList_01 = projectPersonnelList()
CoreServer_projectPersonnelList_01.url = Customer_url + "/biz/reserve/projectPersonnelList"
CoreServer_projectPersonnelList_01.X_Type = APP_a["X-Type"]
CoreServer_projectPersonnelList_01.projectId = APP_a["projectId"]
CoreServer_projectPersonnelList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_projectPersonnelList_01.code = APP_a["error_code_correct"]
#4.2.2
CoreServer_personnelProjectList_01 = personnelProjectList()
CoreServer_personnelProjectList_01.url = Customer_url + "/biz/reserve/personnelProjectList"
CoreServer_personnelProjectList_01.X_Type = APP_a["X-Type"]
CoreServer_personnelProjectList_01.personnelId = APP_a["personnelId"]
CoreServer_personnelProjectList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_projectPersonnelList_01.code = APP_a["error_code_correct"]
#4.2.3
CoreServer_orderSave_01 = orderSave()
CoreServer_orderSave_01.url = Customer_url +"/biz/reserve/orderSave"
CoreServer_orderSave_01.X_Type = APP_a["X-Type"]
CoreServer_orderSave_01.projectId = APP_a["projectId"]
CoreServer_orderSave_01.personnelId = APP_a["personnelId"]
CoreServer_orderSave_01.customerId = APP_a["customerId"]
CoreServer_orderSave_01.makeStartDate = APP_a["makeStartDate"]
CoreServer_orderSave_01.makeEndDate = APP_a["makeEndDate"]
CoreServer_orderSave_01.priceType = APP_a["priceType"]
CoreServer_orderSave_01.reserveName = APP_a["reserveName"]
CoreServer_orderSave_01.reservePhone = APP_a["reservePhone"]
#exp
CoreServer_orderSave_01.code = APP_a["error_code_correct"]
#4.2.4
CoreServer_cancelOrder_01 = cancelOrder()
CoreServer_cancelOrder_01.url = Customer_url + "/biz/reserve/cancelOrder"
CoreServer_cancelOrder_01.X_Type = APP_a["X-Type"]
CoreServer_cancelOrder_01.orderNo = APP_a["orderNo"]
CoreServer_cancelOrder_01.customerId = APP_a["customerId"]
#exp
CoreServer_cancelOrder_01.code = APP_a["error_code_correct"]