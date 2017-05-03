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
    "orderNo":"DD1012706542136455067",#订单编号
    "payCode":"QR7543166741178590773",#支付码
    "makeStartDate":"2017-05-28 12:00:00",#预约开始时间
    "makeEndDate":"2017-03-25 12:30:00",#预约结束时间
    "priceType":1,#价格类型,0(单价)/1(疗程)
    "reserveName":"xing",
    "reservePhone":"13051175683",
    "customerId":42,#顾客id
    "remark":"hello",
    "rankId":1,
    "activityId":163,
    "longitude":"120.635753",
    "latitude":"31.267955",
    "openId":"oV4G3v3Na7WiI6hP7JEbZgXqAi2I",
    "page":1,
    "commentLevel":3,
    "approveStatus":3,
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
CoreServer_searchProjectList_01 = searchProjectList()
CoreServer_searchProjectList_01.url = Customer_url + "/biz/reserve/personnelProjectList"
CoreServer_searchProjectList_01.X_Type = APP_a["X-Type"]
CoreServer_searchProjectList_01.personnelId = APP_a["personnelId"]
CoreServer_searchProjectList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_searchProjectList_01.code = APP_a["error_code_correct"]
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
#4.2.5
CoreServer_applyCancelOrder_01 = applyCancelOrder()
CoreServer_applyCancelOrder_01.url = Customer_url + "/biz/reserve/applyCancelOrder"
CoreServer_applyCancelOrder_01.X_Type = APP_a["X-Type"]
CoreServer_applyCancelOrder_01.orderNo = APP_a["orderNo"]
CoreServer_applyCancelOrder_01.customerId = APP_a["customerId"]
#exp
CoreServer_applyCancelOrder_01.code = APP_a["error_code_correct"]
#4.2.6
CoreServer_personnelServeProject_01 = personnelServeProject()
CoreServer_personnelServeProject_01.url = Customer_url +"/biz/reserve/personnelServeProject"
CoreServer_personnelServeProject_01.X_Type = APP_a["X-Type"]
CoreServer_personnelServeProject_01.projectId  =APP_a["projectId"]
CoreServer_personnelServeProject_01.personnelId = APP_a["personnelId"]
#exp
CoreServer_personnelServeProject_01.code =APP_a["error_code_correct"]
#************************************************4.3***********************************************************
#4.3.1.1
CoreServer_hotProject_01 = hotProject()
CoreServer_hotProject_01.url = Customer_url + "/biz/index/hotProject"
CoreServer_hotProject_01.X_Type = APP_a["X-Type"]
CoreServer_hotProject_01.longitude = APP_a["longitude"]
CoreServer_hotProject_01.latitude = APP_a["latitude"]
CoreServer_hotProject_01.cityId = APP_a["cityId"]
CoreServer_hotProject_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_hotProject_01.code = APP_a["error_code_correct"]
#4.3.1.2
CoreServer_searchProjectList_01 = searchProjectList()
CoreServer_searchProjectList_01.url = Customer_url + "/biz/index/searchProjectList"
CoreServer_searchProjectList_01.X_Type = APP_a["X-Type"]
CoreServer_searchProjectList_01.cityId = APP_a["cityId"]
CoreServer_searchProjectList_01.longitude = APP_a["longitude"]
CoreServer_searchProjectList_01.latitude = APP_a["latitude"]
CoreServer_searchProjectList_01.page = APP_a["page"]
CoreServer_searchProjectList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_searchProjectList_01.code = APP_a["error_code_correct"]
#4.3.1.3
CoreServer_projectDetails_01 = projectDetails()
CoreServer_projectDetails_01.url = Customer_url + "/biz/index/projectDetails"
CoreServer_projectDetails_01.X_Type = APP_a["X-Type"]
CoreServer_projectDetails_01.id = APP_a["projectId"]
#ep
CoreServer_projectDetails_01.code = APP_a["error_code_correct"]
#4.3.1.4
CoreServer_projectCommentGroupNum_01 = projectCommentGroupNum()
CoreServer_projectCommentGroupNum_01.url = Customer_url + "/biz/index/projectCommentGroupNum"
CoreServer_projectCommentGroupNum_01.X_Type = APP_a["X-Type"]
CoreServer_projectCommentGroupNum_01.projectId = APP_a["projectId"]
#ep
CoreServer_projectCommentGroupNum_01.code = APP_a["error_code_correct"]
#4.3.1.5
CoreServer_projectCommentList_01 = projectCommentList()
CoreServer_projectCommentList_01.url = Customer_url +"/biz/index/projectCommentList"
CoreServer_projectCommentList_01.X_Type = APP_a["X-Type"]
CoreServer_projectCommentList_01.projectId = APP_a["projectId"]
CoreServer_projectCommentList_01.commentLevel = APP_a["commentLevel"]
CoreServer_projectCommentList_01.pageSize = APP_a["pageSize"]
#exo
CoreServer_projectCommentList_01.code = APP_a["error_code_correct"]

#4.3.2.1
CoreServer_hotPersonnel_01 = hotPersonnel()
CoreServer_hotPersonnel_01.url = Customer_url + "/biz/index/hotPersonnel"
CoreServer_hotPersonnel_01.X_Type = APP_a["X-Type"]
CoreServer_hotPersonnel_01.longitude = APP_a["longitude"]
CoreServer_hotPersonnel_01.latitude = APP_a["latitude"]
CoreServer_hotPersonnel_01.cityId = APP_a["cityId"]
CoreServer_hotPersonnel_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_hotPersonnel_01.code = APP_a["error_code_correct"]
#4.3.2.2
CoreServer_searchPersonnelList_01 = searchProjectList()
CoreServer_searchProjectList_01.url = Customer_url + "/biz/index/searchPersonnelList"
CoreServer_searchProjectList_01.X_Type = APP_a["X-Type"]
CoreServer_searchProjectList_01.cityId = APP_a["cityId"]
CoreServer_searchProjectList_01.longitude =APP_a["longitude"]
CoreServer_searchProjectList_01.latitude = APP_a["latitude"]
CoreServer_searchProjectList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_searchProjectList_01.code = APP_a["error_code_correct"]
#4.3.2.3
CoreServer_personnelDetail_01 = personnelDetail()
CoreServer_personnelDetail_01.url = Customer_url + "/biz/index/personnelDetail"
CoreServer_personnelDetail_01.X_Type = APP_a["X-Type"]
CoreServer_personnelDetail_01.id = APP_a["personnelId"]
#exp
CoreServer_personnelDetail_01.code = APP_a["error_code_correct"]
#4.3.2.4
CoreServer_personnelProjectList_01 = personnelProjectList()
CoreServer_personnelProjectList_01.url = Customer_url + "/biz/index/personnelProjectList"
CoreServer_personnelProjectList_01.X_Type = APP_a["X-Type"]
CoreServer_personnelProjectList_01.shopId = APP_a["shopId"]
CoreServer_personnelProjectList_01.personnelId = APP_a["personnelId"]
CoreServer_personnelProjectList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_personnelProjectList_01.code = APP_a["error_code_correct"]
#4.3.2.5
CoreServer_personnelCommentGroupNum_01  = personnelCommentGroupNum()
CoreServer_personnelCommentGroupNum_01.url = Customer_url +"/biz/index/personnelCommentGroupNum "
CoreServer_personnelCommentGroupNum_01.X_Type = APP_a["X-Type"]
CoreServer_personnelCommentGroupNum_01.personnelId = APP_a["personnelId"]
#exp
CoreServer_personnelCommentGroupNum_01.code = APP_a["error_code_correct"]
#4.3.2.6
CoreServer_personnelCommentList_01 = personnelCommentList()
CoreServer_personnelCommentList_01.url = Customer_url + "/biz/index/personnelCommentList"
CoreServer_personnelCommentList_01.personnelId = APP_a["personnelId"]
CoreServer_personnelCommentList_01.commentLevel = APP_a["commentLevel"]
CoreServer_personnelCommentList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_personnelCommentList_01.code = APP_a["error_code_correct"]
#***********************************************4.4**************************************************
#4.4.1
CoreServer_reserveProjectRecord_01 = reserveProjectRecord()
CoreServer_reserveProjectRecord_01.url = Customer_url + "/biz/order/reserveProjectRecord"
CoreServer_reserveProjectRecord_01.X_Type = APP_a["X-Type"]
CoreServer_reserveProjectRecord_01.customerId = APP_a["customerId"]
CoreServer_reserveProjectRecord_01.longitude = APP_a["longitude"]
CoreServer_reserveProjectRecord_01.latitude = APP_a["latitude"]
CoreServer_reserveProjectRecord_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_reserveProjectRecord_01.code = APP_a["error_code_correct"]

#4.4.2
CoreServer_reservePersonnelRecord_01 = reservePersonnelRecord()
CoreServer_reservePersonnelRecord_01.url = Customer_url + "/biz/order/reservePersonnelRecord"
CoreServer_reservePersonnelRecord_01.X_Type = APP_a["X-Type"]
CoreServer_reservePersonnelRecord_01.customerId = APP_a["customerId"]
CoreServer_reservePersonnelRecord_01.longitude = APP_a["longitude"]
CoreServer_reservePersonnelRecord_01.latitude = APP_a["latitude"]
CoreServer_reservePersonnelRecord_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_reservePersonnelRecord_01.code = APP_a["error_code_correct"]

#4.4.3
CoreServer_orderGroupNum_01 = orderGroupNum()
CoreServer_orderGroupNum_01.url = Customer_url + "/biz/order/orderGroupNum"
CoreServer_orderGroupNum_01.X_Type = APP_a["X-Type"]
CoreServer_orderGroupNum_01.customerId = APP_a["customerId"]
#exp
CoreServer_orderGroupNum_01.code= APP_a["error_code_correct"]
#4.4.4
CoreServer_myOderList_01 = myOrderList()
CoreServer_myOderList_01.url = Customer_url + "/biz/order/myOrderList"
CoreServer_myOderList_01.X_Type = APP_a["X-Type"]
CoreServer_myOderList_01.customerId = APP_a["customerId"]
CoreServer_myOderList_01.approveStatus =  APP_a["approveStatus"]
CoreServer_myOderList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_myOderList_01.code = APP_a["error_code_correct"]
#4.4.5
CoreServer_orderDetail_01 = orderDetail()
CoreServer_orderDetail_01.url = Customer_url + "/biz/order/orderDetail"
CoreServer_orderDetail_01.X_Type = APP_a["X-Type"]
CoreServer_orderDetail_01.customerId = APP_a["customerId"]
CoreServer_orderDetail_01.orderNo = APP_a["orderNo"]
#exp
CoreServer_orderDetail_01.code = APP_a["error_code_correct"]
#4.4.6
CoreServer_payQRDetail_01 = payQRDetail()
CoreServer_payQRDetail_01.url = Customer_url + "/biz/order/payQRDetail"
CoreServer_payQRDetail_01.X_Type = APP_a["X-Type"]
CoreServer_payQRDetail_01.customerId = APP_a["customerId"]
CoreServer_payQRDetail_01.orderNo = APP_a["orderNo"]
#exp
CoreServer_payQRDetail_01.code = APP_a["error_code_correct"]
#4.4.7
CoreServer_orderComment_01  = orderComment()
CoreServer_orderComment_01.url = Customer_url + "/bin/order/orderComment"
CoreServer_orderComment_01.X_Type = APP_a["X-Type"]
CoreServer_orderComment_01.orderNo = APP_a["orderNo"]
# CoreServer_orderComment_01.
