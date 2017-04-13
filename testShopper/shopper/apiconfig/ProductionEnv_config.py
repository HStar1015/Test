# -*- coding: utf-8 -*-
from ApiClass import *

APP_a = {
    "error_code_correct" :1,
    "error_code_fail":0,
    "phone":"15651966757",
    "shopId":15,#15651966757--商家id
    "mendianId":91,#门店id
    "deleteShopId":87,#删除门店id
    "password":"0adc3949ba59abbe56e057f20f883ee1",
    "X-Type":1,
    "provinceId":320000,#jiangsu
    "cityId":320500,#suzhou
    "areaId":320506,#wuzhongqu
    "registrationId":861759031496572,#EVL00
    "shopName":"Test",
    "shortName":"T",
    "description":"QWERTYUIOPASDFGHJKL",
    "address":"suzhou",
    "files":"",
    "projectName":"补水",
    "groupNo":"1002",#项目编号
    "unitPrice":"10.00",
    "coursePrice":"100",
    "courseRemark":"test test",
    "duration":"20",
    "applyPerson":"young man",
    "brand":"测试",
    "noticeMatters":"test test test",
    "projectId":"142",#项目ID
    "fileUuid":"5230f677909648d89dadc37a25604a31",
    "picCount":5,#图片数量
    "pageSize":100,#分页数量
    "personneId":"18",#员工id
    "commentLevel_1":"1",#差评
    "commentLevel_2":"2",#中评
    "commentLevel_3":"3",#好评
    "commentLevel_all":"",#全部评价
    "customerId":"43",#顾客id
    "rankId":"1",#备注级别id
    "paymentMode_alipay":"alipay",#提现付款方式--支付宝
    "paymentMode_card":"card",#提现付款方式---银行卡
    "price":"0.00",#提现金额
    "putApplyId":"92",#提现记录id
    "incomeId":"91",#进账记录id
    "bunkCount": "3",#床位数
    "projectAverageDuration": "45",#项目平均操作时长
    "workStartDate": "09:00",#上班时间
    "workEndDate": "21:00",#下班时间
    "personnelCount": "15",#美容师数量
    "customerAverageExpense": "1000",#顾客平均年消费
    "activeCustomerCount": "10",#活跃顾客数量
    "mainProjectAverageDuration": "25",#主项目平均操作时长
    "monthShopTurnover":"20000",#店月营业额
    "dayShopCustomerCount":"20",#店日进店量
    "personnelCount":"10",#美容师数量
    "monthTookeenCount":"20",#现在新顾客
    "yearShopTurnover":"1000000",#店年营业额
    "activityName":"TEST",#活动名称
    "activityStartDate":"2017-04-05 00:00:00",#活动开始时间
    "activityEndDate":"2017-04-18 00:00:00",#活动结束时间
    "activityUnitPrice":"0.01",#活动单价
    "activityCoursePrice":"1",#活动疗程价格
    "activityId":"164",#活动id
    "day":"2017-04-12",
    "month":"2017-04",
    "summarizeId":"2",
    "planId":"23",
    "cardId":16,
}
Base_url = "https://www.iumer.cn/umer/webService"
Shop_url = Base_url +"/shop"

#************************2.1*******************************
#2.1.1注册
CoreServer_register_01 = register()
#input
CoreServer_register_01.url = Shop_url +"/sys/business/register"
CoreServer_register_01.phone = APP_a["phone"]
CoreServer_register_01.password = APP_a["password"]
CoreServer_register_01.authCode = 123456
CoreServer_register_01.inviteCode = "QWERTYU"
CoreServer_register_01.X_Type = APP_a["X-Type"]
#expect
CoreServer_register_01.code = APP_a["error_code_correct"]

#2.1.2登录
CoreServer_login_01 = login()
#input
CoreServer_login_01.url = Shop_url + "/sys/business/login"
CoreServer_login_01.phone = APP_a["phone"]
CoreServer_login_01.password = APP_a["password"]
CoreServer_login_01.X_Type = APP_a["X-Type"]
#expect
CoreServer_login_01.code = APP_a["error_code_correct"]
CoreServer_login_01.shop_id =""
CoreServer_login_01.shop_name  = ""
CoreServer_login_01.shop_phone = ""
CoreServer_login_01.shop_header = ""
CoreServer_login_01.token = ""
CoreServer_login_01.inviteStatus = ""

#2.1.3申请邀请码
#req
CoreServer_applyInvite_01 = applyInvite()
CoreServer_applyInvite_01.url = Shop_url +"/sys/business/applyInvite"
CoreServer_applyInvite_01.name = "hanxing"
CoreServer_applyInvite_01.phone = "15651966755"
CoreServer_applyInvite_01.provinceId = APP_a["provinceId"]
CoreServer_applyInvite_01.areaId = APP_a["areaId"]
CoreServer_applyInvite_01.cityId = APP_a["cityId"]
CoreServer_applyInvite_01.X_Type = APP_a["X-Type"]
#exp
CoreServer_applyInvite_01.code = APP_a["error_code_correct"]

#2.1.4修改商家信息
#req
CoreServer_updateInfo_01 = updateInfo()
CoreServer_updateInfo_01.url = Shop_url +"/sys/business/updateInfo"
CoreServer_updateInfo_01.id = APP_a["shopId"]
#exp
CoreServer_updateInfo_01.code = APP_a["error_code_correct"]

#2.1.5获取商家信息
#req
CoreServer_businessInfo_01 = businessInfo()
CoreServer_businessInfo_01.url = Shop_url+"/sys/business/businessInfo"
CoreServer_businessInfo_01.id = APP_a["shopId"]
CoreServer_businessInfo_01.X_Type = APP_a["X-Type"]
#exp
CoreServer_businessInfo_01.code = APP_a["error_code_correct"]

#2.1.6更新设备ID
#req
CoreServer_updateRegistrationId_01 = updateRegistrationId()
CoreServer_updateRegistrationId_01.url = Shop_url +"/sys/business/updateRegistrationId"
CoreServer_updateRegistrationId_01.id = APP_a["shopId"]
CoreServer_updateRegistrationId_01.registrationId = APP_a["registrationId"]
CoreServer_updateRegistrationId_01.X_Type = APP_a["X-Type"]
#exp
CoreServer_updateRegistrationId_01.code = APP_a["error_code_correct"]
#************************2.2*******************************
#2.2.1
#req
CoreServer_saveShop_01 = saveShop()
CoreServer_saveShop_01.url = Shop_url +"/sys/user/saveShop"
CoreServer_saveShop_01.X_Type = APP_a["X-Type"]
CoreServer_saveShop_01.businessId = APP_a["shopId"]
CoreServer_saveShop_01.phone = APP_a["phone"]
CoreServer_saveShop_01.shopName = APP_a["shopName"]
CoreServer_saveShop_01.shortName = APP_a["shortName"]
CoreServer_saveShop_01.description = APP_a["description"]
CoreServer_saveShop_01.provinceId = APP_a["provinceId"]
CoreServer_saveShop_01.cityId = APP_a["cityId"]
CoreServer_saveShop_01.areaId = APP_a["areaId"]
CoreServer_saveShop_01.address = APP_a["address"]
CoreServer_saveShop_01.files = APP_a["files"]
#exp
CoreServer_saveShop_01.code = APP_a["error_code_correct"]
#2.2.2
CoreServer_saveShop_01 = saveShop()
CoreServer_saveShop_01.url = Shop_url +"/sys/user/updateInfo"
CoreServer_saveShop_01.X_Type = APP_a["X-Type"]
CoreServer_saveShop_01.businessId = APP_a["shopId"]
CoreServer_saveShop_01.phone = APP_a["phone"]
CoreServer_saveShop_01.shopName = APP_a["shopName"]
CoreServer_saveShop_01.shortName = APP_a["shortName"]
CoreServer_saveShop_01.description = APP_a["description"]
CoreServer_saveShop_01.provinceId = APP_a["provinceId"]
CoreServer_saveShop_01.cityId = APP_a["cityId"]
CoreServer_saveShop_01.areaId = APP_a["areaId"]
CoreServer_saveShop_01.address = APP_a["address"]
CoreServer_saveShop_01.files = APP_a["files"]
#exp
CoreServer_saveShop_01.code = APP_a["error_code_correct"]
#2.2.3
CoreServer_shopList_01 = shopList()
#input
CoreServer_shopList_01.url = Shop_url +"/sys/user/shopList"
CoreServer_shopList_01.businessId = APP_a["shopId"]
CoreServer_shopList_01.X_Type = APP_a["X-Type"]
#exp
CoreServer_shopList_01.code = APP_a["error_code_correct"]
#2.2.4
CoreServer_shopInfo_01 = shopInfo()
#input
CoreServer_shopInfo_01.X_Type  = APP_a["X-Type"]
CoreServer_shopList_01.url = Shop_url +"/sys/user/shopInfo"
CoreServer_shopList_01.id = APP_a["mendianId"]
#exp
CoreServer_shopList_01.code = APP_a["error_code_correct"]
#2.2.5
CoreServer_deleteShop_01 = deleteShop()
#input
CoreServer_deleteShop_01.url = Shop_url +"/sys/user/deleteShop"
CoreServer_deleteShop_01.X_Type = APP_a["X-Type"]
CoreServer_deleteShop_01.id = APP_a["deleteShopId"]
CoreServer_deleteShop_01.businessId = APP_a["shopId"]
#exp
CoreServer_deleteShop_01.code = APP_a["error_code_correct"]
#2.2.6.1
CoreServer_shopStatics_01 = shopStatics()
CoreServer_shopStatics_01.url = Shop_url +"/biz/shopdata/shopStatistics"
CoreServer_shopStatics_01.X_Type = APP_a["X-Type"]
CoreServer_shopStatics_01.shopId = APP_a["mendianId"]
#exp
CoreServer_shopStatics_01.code = APP_a["error_code_correct"]
#2.2.6.2
CoreServer_saleStatistics_01 = saleStatistics()
CoreServer_saleStatistics_01.url = Shop_url +"/biz/shopdata/saleStatistics"
CoreServer_saleStatistics_01.X_Type = APP_a["X-Type"]
CoreServer_saleStatistics_01.shopId = APP_a["mendianId"]
#exp
CoreServer_saleStatistics_01.code = APP_a["error_code_correct"]
#2.2.6.3
CoreServer_newCustomerStatistics_01 = newCustomerStatistics()
CoreServer_newCustomerStatistics_01.url = Shop_url +"/biz/shopdata/newCustomerStatistics"
CoreServer_newCustomerStatistics_01.X_Type = APP_a["X-Type"]
CoreServer_newCustomerStatistics_01.shopId = APP_a["mendianId"]
#exp
CoreServer_newCustomerStatistics_01.code = APP_a["error_code_correct"]
#2.2.6.4
CoreServer_projectSaleStatistics_01 = projectSaleStatistics()
CoreServer_projectSaleStatistics_01.url = Shop_url +"/biz/shopdata/projectSaleStatistics"
CoreServer_projectSaleStatistics_01.X_Type = APP_a["X-Type"]
CoreServer_projectSaleStatistics_01.shopId = APP_a["mendianId"]
#exp
CoreServer_projectSaleStatistics_01.code = APP_a["error_code_correct"]
#************************2.3*******************************
#2.3.1
CoreServer_addProject_01 = addProject()
#input
CoreServer_addProject_01.url = Shop_url +"/biz/project/addProject"
CoreServer_addProject_01.X_Type = APP_a["X-Type"]
CoreServer_addProject_01.businessId = APP_a["shopId"]
CoreServer_addProject_01.shopIds =APP_a["mendianId"]
CoreServer_addProject_01.projectName = APP_a["projectName"]
CoreServer_addProject_01.groupNo = APP_a["groupNo"]
CoreServer_addProject_01.unitPrice = APP_a["unitPrice"]
CoreServer_addProject_01.coursePrice = APP_a["coursePrice"]
CoreServer_addProject_01.courseRemark = APP_a["courseRemark"]
CoreServer_addProject_01.duration = APP_a["duration"]
CoreServer_addProject_01.description = APP_a["description"]
CoreServer_addProject_01.applyPerson = APP_a["applyPerson"]
CoreServer_addProject_01.brand = APP_a["brand"]
CoreServer_addProject_01.noticeMatters = APP_a["noticeMatters"]
CoreServer_addProject_01.files = APP_a["files"]
#exp
CoreServer_addProject_01.code = APP_a["error_code_correct"]
#2.3.2
CoreServer_deleteProject_01 = deleteProject()
CoreServer_deleteProject_01.url = Shop_url + "/biz/project/deleteProject"
CoreServer_deleteProject_01.X_Type = APP_a["X-Type"]
CoreServer_deleteProject_01.id = APP_a["projectId"]
#exp
CoreServer_deleteProject_01.code =APP_a["error_code_correct"]
#2.3.3
CoreServer_editProject_01 = editProject()
#input
CoreServer_editProject_01.url =Shop_url +"/biz/project/editProject "
CoreServer_editProject_01.X_Type = APP_a["X-Type"]
CoreServer_editProject_01.id = APP_a["projectId"]
CoreServer_editProject_01.projectName = APP_a["projectName"]
CoreServer_editProject_01.groupNo = APP_a["groupNo"]
CoreServer_editProject_01.unitPrice = APP_a["unitPrice"]
CoreServer_editProject_01.coursePrice = APP_a["coursePrice"]
CoreServer_editProject_01.courseRemark = APP_a["courseRemark"]
CoreServer_editProject_01.duration = APP_a["duration"]
CoreServer_editProject_01.description = APP_a["description"]
CoreServer_editProject_01.applyPerson = APP_a["applyPerson"]
CoreServer_editProject_01.brand = APP_a["brand"]
CoreServer_editProject_01.noticeMatters = APP_a["noticeMatters"]
CoreServer_editProject_01.fileUuid = APP_a["fileUuid"]
CoreServer_editProject_01.files = APP_a["files"]
CoreServer_editProject_01.picCount = APP_a["picCount"]
#exp
CoreServer_editProject_01.code= APP_a["error_code_correct"]
#2.3.4
CoreServer_projectList_01 = projectList()
CoreServer_projectList_01.url = Shop_url +"/biz/project/projectList"
CoreServer_projectList_01.shopId = APP_a["mendianId"]
CoreServer_projectList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_projectList_01.code = APP_a["error_code_correct"]
#2.3.5
CoreServer_projectDetails_01 = projectDetails()
CoreServer_projectDetails_01.url = Shop_url +"/biz/project/projectDetails"
CoreServer_projectDetails_01.X_Type = APP_a["X-Type"]
CoreServer_projectDetails_01.id = APP_a["projectId"]
#exp
CoreServer_projectDetails_01.code = APP_a["error_code_correct"]
#2.3.6
CoreServer_copyProject_01 = copyProject()
CoreServer_copyProject_01.url = Shop_url +"/biz/project/copyProject "
CoreServer_copyProject_01.X_Type = APP_a["X-Type"]
CoreServer_copyProject_01.projectIds = APP_a["projectId"]
CoreServer_copyProject_01.shopId = APP_a["mendianId"]
CoreServer_copyProject_01.businessId = APP_a["shopId"]
#exp
CoreServer_copyProject_01.code = APP_a["error_code_correct"]
#************************2.4*******************************
#2.4.1
CoreServer_pushInvitation_01 = pushInvitation()
#input
CoreServer_pushInvitation_01.url = Shop_url +"/biz/personnel/pushInvitation"
CoreServer_pushInvitation_01.personnelPhone = APP_a["phone"]
CoreServer_pushInvitation_01.businessId = APP_a["shopId"]
CoreServer_pushInvitation_01.shopId = APP_a["mendianId"]
CoreServer_pushInvitation_01.phone = APP_a["phone"]
CoreServer_pushInvitation_01.X_Type = APP_a["X-Type"]
#exp
CoreServer_pushInvitation_01.code = APP_a["error_code_correct"]
#2.4.2
CoreServer_personnelList_01 = personnelList()
CoreServer_personnelList_01.url = Shop_url +"/biz/personnel/personnelList"
CoreServer_personnelList_01.businessId = APP_a["shopId"]
#CoreServer_personnelList_01.shopId = APP_a["mendianId"]
CoreServer_personnelList_01.pageSize = APP_a["pageSize"]
CoreServer_deleteProject_01.X_Type = APP_a["X-Type"]
#exp
CoreServer_personnelList_01.code = APP_a["error_code_correct"]
#2.4.3
CoreServer_personnelDetails_01 = personnelDetails()
CoreServer_personnelDetails_01.X_Type = APP_a["X-Type"]
CoreServer_personnelDetails_01.url = Shop_url +"/biz/personnel/personnelDetails"
CoreServer_personnelDetails_01.id = APP_a["personneId"]
#exp
CoreServer_personnelDetails_01.code = APP_a["error_code_correct"]
#2.4.4
CoreServer_unbind_01 = unbind()
#input
CoreServer_unbind_01.url = Shop_url +"/biz/personnel/unbind"
CoreServer_unbind_01.id = APP_a["personneId"]
CoreServer_unbind_01.businessId = APP_a["shopId"]
CoreServer_unbind_01.X_Type = APP_a["X-Type"]
#exp
CoreServer_unbind_01.code = APP_a["error_code_correct"]
#2.4.5
CoreServer_allocationPersonnel_01 = allocationPersonnel()
#input
CoreServer_allocationPersonnel_01.url = Shop_url +"/biz/personnel/allocationPersonnel"
CoreServer_allocationPersonnel_01.businessId = 15
CoreServer_allocationPersonnel_01.shopId = 91
CoreServer_allocationPersonnel_01.personnelIds = 18
CoreServer_allocationPersonnel_01.X_Type = APP_a["X-Type"]
#exp
CoreServer_allocationPersonnel_01.code = APP_a["error_code_correct"]
#2.4.6.1
CoreServer_commentGroupNum_01 = commentGroupNum()
CoreServer_commentGroupNum_01.url = Shop_url +"/biz/personnel/commentGroupNum"
CoreServer_commentGroupNum_01.personnelId = APP_a["personneId"]
CoreServer_commentGroupNum_01.X_Type = APP_a["X-Type"]
#exp
CoreServer_commentGroupNum_01.code = APP_a["error_code_correct"]
#2.4.6.2
CoreServer_commentList_01 = commentList()
CoreServer_commentList_01.url = Shop_url +"/biz/personnel/commentList"
CoreServer_commentList_01.personnelId = APP_a["personneId"]
CoreServer_commentList_01.commentLevel = APP_a["commentLevel_all"]
CoreServer_commentList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_commentList_01.code = APP_a["error_code_correct"]
#2.4.7.1
CoreServer_daySummarizeList_01 = daySummarizeList()
CoreServer_daySummarizeList_01.url = Shop_url +"/biz/personnel/daySummarizeList"
CoreServer_daySummarizeList_01.day = APP_a["day"]
CoreServer_daySummarizeList_01.shopId = APP_a["mendianId"]
CoreServer_daySummarizeList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_daySummarizeList_01.code = APP_a["error_code_correct"]
#2.4.7.2
CoreServer_daySummarizeDetail_01 = daySummarizeDetail()
CoreServer_daySummarizeDetail_01.url = Shop_url +"/biz/personnel/daySummarizeDetail"
CoreServer_daySummarizeDetail_01.X_Type = APP_a["X-Type"]
CoreServer_daySummarizeDetail_01.summarizeId = APP_a["summarizeId"]
#exp
CoreServer_daySummarizeDetail_01.code = APP_a["error_code_correct"]
#2.4.7.3
CoreServer_monthPlanList_01 = monthPlanList()
CoreServer_monthPlanList_01.url = Shop_url +"/biz/personnel/monthPlanList"
CoreServer_monthPlanList_01.X_Type = APP_a["X-Type"]
CoreServer_monthPlanList_01.month = APP_a["month"]
CoreServer_monthPlanList_01.shopId = APP_a["mendianId"]
CoreServer_monthPlanList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_monthPlanList_01.code = APP_a["error_code_correct"]
#2.4.7.4
CoreServer_monthDetail_01 = monthPlanDetail()
CoreServer_monthDetail_01.url = Shop_url +"/biz/personnel/monthPlanDetail"
CoreServer_monthDetail_01.X_Type = APP_a["X-Type"]
CoreServer_monthDetail_01.planId = APP_a["planId"]
#exp
CoreServer_monthDetail_01.code = APP_a["error_code_correct"]
#2.4.8.1
CoreServer_operationCaseList_01 = operationCaseList()
CoreServer_operationCaseList_01.url = Shop_url +"/biz/personnel/operationCaseList"
CoreServer_operationCaseList_01.X_Type = APP_a["X-Type"]
CoreServer_operationCaseList_01.shopId = APP_a["mendianId"]
#exp
CoreServer_operationCaseList_01.code = APP_a["error_code_correct"]
#2.4.8.2
CoreServer_operationDetail_01 = operationCaseDetail()
CoreServer_operationDetail_01.url = Shop_url +"/biz/personnel/operationCaseDetail"
CoreServer_operationDetail_01.X_Type = APP_a["X-Type"]
CoreServer_operationDetail_01.shopId = APP_a["mendianId"]
CoreServer_operationDetail_01.month = APP_a["month"]
#exp
CoreServer_operationDetail_01.code = APP_a["error_code_correct"]
#***************************************2.5*******************************
#2.5.1
CoreServer_customerList_01 = customerList()
CoreServer_customerList_01.url = Shop_url +"/biz/customer/customerList"
CoreServer_customerList_01.shopId = APP_a["mendianId"]
CoreServer_customerList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_customerList_01.code = APP_a["error_code_correct"]
#2.5.2
CoreServer_customerDetails_01 = customerDetails()
CoreServer_customerDetails_01.url = Shop_url +"/biz/customer/customerDetails"
CoreServer_customerDetails_01.X_Type = APP_a["X-Type"]
CoreServer_customerDetails_01.shopId = APP_a["mendianId"]
CoreServer_customerDetails_01.customerId = APP_a["customerId"]
#exp
CoreServer_customerDetails_01.code = APP_a["error_code_correct"]
#2.5.3
CoreServer_allocationCustomer_01 = allocationCustomer()
CoreServer_allocationCustomer_01.url = Shop_url +"/biz/customer/allocationCustomer"
CoreServer_allocationCustomer_01.X_Type = APP_a["X-Type"]
CoreServer_allocationCustomer_01.shopId = APP_a["mendianId"]
CoreServer_allocationCustomer_01.personnelId = APP_a["personneId"]
CoreServer_allocationCustomer_01.customerId = APP_a["customerId"]
#exp
CoreServer_allocationCustomer_01.code = APP_a["error_code_correct"]
#2.5.4
CoreServer_expenseRecord_01  = expenseRecord()
CoreServer_expenseRecord_01.url = Shop_url +"/biz/customer/expenseRecord"
CoreServer_expenseRecord_01.X_Type = APP_a["X-Type"]
CoreServer_expenseRecord_01.customerId = APP_a["customerId"]
CoreServer_expenseRecord_01.shopId = APP_a["mendianId"]
CoreServer_expenseRecord_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_expenseRecord_01.code = APP_a["error_code_correct"]
#2.5.5
CoreServer_expenseProject_01  = expenseProject()
CoreServer_expenseProject_01.url = Shop_url +"/biz/customer/expenseProject"
CoreServer_expenseProject_01.X_Type = APP_a["X-Type"]
CoreServer_expenseProject_01.customerId = APP_a["customerId"]
CoreServer_expenseProject_01.shopId = APP_a["mendianId"]
CoreServer_expenseProject_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_expenseProject_01.code = APP_a["error_code_correct"]
#2.5.6
CoreServer_changeRank_01 = changeRank()
CoreServer_changeRank_01.url = Shop_url +"/biz/customer/changeRank"
CoreServer_changeRank_01.shopId = APP_a["shopId"]
CoreServer_changeRank_01.rankId = APP_a["rankId"]
CoreServer_changeRank_01.customerIds = APP_a["customerId"]
#exp
CoreServer_changeRank_01.code = APP_a["error_code_correct"]
#2.5.7
CoreServer_rankInfoList_01 = rankInfoList()
CoreServer_rankInfoList_01.url = Shop_url +"/biz/customer/rankInfoList"
CoreServer_rankInfoList_01.shopId = APP_a["shopId"]
CoreServer_rankInfoList_01.X_Type = APP_a["X-Type"]
#exp
CoreServer_rankInfoList_01.code = APP_a["error_code_correct"]
#2.5.8.1
CoreServer_customerCardList_01 = customerCardList()
CoreServer_customerCardList_01.url = Shop_url + "/biz/customer/customerCardList"
CoreServer_customerCardList_01.X_Type = APP_a["X-Type"]
CoreServer_customerCardList_01.shopId = APP_a["mendianId"]
CoreServer_customerCardList_01.customerId = APP_a["customerId"]
CoreServer_customerCardList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_customerCardList_01.code = APP_a["error_code_correct"]
#2.5.8.2
CoreServer_cardConsummerDetailList_01 = cardConsummerDetailList()
CoreServer_cardConsummerDetailList_01.url = Shop_url +"/biz/customer/cardConsummerDetailList"
CoreServer_cardConsummerDetailList_01.X_Type = APP_a["X-Type"]
CoreServer_cardConsummerDetailList_01.cardId = APP_a["cardId"]
CoreServer_cardConsummerDetailList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_cardConsummerDetailList_01.code = APP_a["error_code_correct"]
#*****************************************2.6*****************************************
#2.6.1
CoreServer_findAccountBalance_01 = findAccountBalance()
CoreServer_findAccountBalance_01.url = Shop_url +"/biz/account/findAccountBalance"
CoreServer_findAccountBalance_01.X_Type = APP_a["X-Type"]
CoreServer_findAccountBalance_01.businessId = APP_a["shopId"]
#exp
CoreServer_findAccountBalance_01.code = APP_a["error_code_correct"]
#2.6.2
CoreServer_accountRecordList_01 = accountRecordList()
CoreServer_accountRecordList_01.url = Shop_url +"/biz/account/accountRecordList"
CoreServer_accountRecordList_01.businessId = APP_a["shopId"]
CoreServer_accountRecordList_01.pageSize = APP_a["pageSize"]
#exo
CoreServer_accountRecordList_01.code = APP_a["error_code_correct"]
#2.6.3
CoreServer_putApply_01 = putApply()
CoreServer_putApply_01.url = Shop_url + "/biz/account/putApply"
CoreServer_putApply_01.businessId = APP_a["shopId"]
CoreServer_putApply_01.paymentMode = APP_a["paymentMode_alipay"]
CoreServer_putApply_01.price = APP_a["price"]
#exp
CoreServer_putApply_01.code = APP_a["error_code_correct"]
#2.6.4
CoreServer_putRecordDetail_01 = putRecordDetail()
CoreServer_putRecordDetail_01.url= Shop_url +"/biz/account/putRecordDetail"
CoreServer_putRecordDetail_01.id = APP_a["putApplyId"]
CoreServer_putRecordDetail_01.X_Type = APP_a["X-Type"]
#exp
CoreServer_putRecordDetail_01.code = APP_a["error_code_correct"]
#2.6.5
CoreServer_incomeRecordDetail_01 = incomeRecordDetail()
CoreServer_incomeRecordDetail_01.url = Shop_url +"/biz/account/incomeRecordDetail"
CoreServer_incomeRecordDetail_01.id = APP_a["incomeId"]
#exp
CoreServer_incomeRecordDetail_01.code = APP_a["error_code_correct"]
#**********************************************2.7*****************************************
#2.7.1
CoreServer_shopCapacity_01 = shopCapacity()
CoreServer_shopCapacity_01.url= Shop_url + "/sys/user/shopCapacity"
CoreServer_shopCapacity_01.X_Type = APP_a["X-Type"]
CoreServer_shopCapacity_01.businessId = APP_a["shopId"]
CoreServer_shopCapacity_01.shopId = APP_a["mendianId"]
CoreServer_shopCapacity_01.bunkCount = APP_a["bunkCount"]
CoreServer_shopCapacity_01.projectAverageDuration = APP_a["projectAverageDuration"]
CoreServer_shopCapacity_01.workStartDate = APP_a["workStartDate"]
CoreServer_shopCapacity_01.workEndDate = APP_a["workEndDate"]
CoreServer_shopCapacity_01.personnelCount = APP_a["personnelCount"]
CoreServer_shopCapacity_01.customerAverageExpense = APP_a["customerAverageExpense"]
CoreServer_shopCapacity_01.activeCustomerCount = APP_a["activeCustomerCount"]
CoreServer_shopCapacity_01.mainProjectAverageDuration = APP_a["mainProjectAverageDuration"]
#exp
CoreServer_shopCapacity_01.code = APP_a["error_code_correct"]
#2.7.2
CoreServer_shopDiagnose_01 = shopDiagnose()
CoreServer_shopDiagnose_01.url = Shop_url +"/sys/user/shopDiagnose"
CoreServer_shopDiagnose_01.X_Type = APP_a["X-Type"]
CoreServer_shopDiagnose_01.businessId = APP_a["shopId"]
CoreServer_shopDiagnose_01.shopId = APP_a["mendianId"]
CoreServer_shopDiagnose_01.monthShopTurnover = APP_a["monthShopTurnover"]
CoreServer_shopDiagnose_01.dayShopCustomerCount = APP_a["dayShopCustomerCount"]
CoreServer_shopDiagnose_01.personnelCount = APP_a["personnelCount"]
CoreServer_shopDiagnose_01.monthTookeenCount = APP_a["monthTookeenCount"]
CoreServer_shopDiagnose_01.yearShopTurnover = APP_a["yearShopTurnover"]
#exp
CoreServer_shopDiagnose_01.code = APP_a["error_code_correct"]
#2.7.3
CoreServer_getShopCapacity_01 = getShopCapacity()
CoreServer_getShopCapacity_01.url = Shop_url +"/sys/user/getShopCapacity"
CoreServer_getShopCapacity_01.businessId  = APP_a["shopId"]
CoreServer_getShopCapacity_01.shopId = APP_a["mendianId"]
#exp
CoreServer_getShopCapacity_01.code = APP_a["error_code_correct"]
#2.7.4
CoreServer_getShopDiagnose_01 = getShopDiagnose()
CoreServer_getShopDiagnose_01.url = Shop_url +"/sys/user/getShopDiagnose"
CoreServer_getShopDiagnose_01.businessId = APP_a["shopId"]
CoreServer_getShopDiagnose_01.shopId = APP_a["mendianId"]
#exp
CoreServer_getShopDiagnose_01.code = APP_a["error_code_correct"]
#**************************************2.8********************************************
#2.8.1
CoreServer_createActivity_01 = createActivity()
CoreServer_createActivity_01.url = Shop_url +"/biz/projectActivity/createActivity"
CoreServer_createActivity_01.businessId = APP_a["shopId"]
CoreServer_createActivity_01.shopId = APP_a["mendianId"]
CoreServer_createActivity_01.activityName = APP_a["activityName"]
CoreServer_createActivity_01.activityStartDate = APP_a["activityStartDate"]
CoreServer_createActivity_01.activityEndDate = APP_a["activityEndDate"]
CoreServer_createActivity_01.activityUnitPrice = APP_a["activityUnitPrice"]
CoreServer_createActivity_01.activityCoursePrice = APP_a["activityCoursePrice"]
CoreServer_createActivity_01.description = APP_a["description"]
CoreServer_createActivity_01.projectIds =APP_a["projectId"]
CoreServer_createActivity_01.X_Type = APP_a["X-Type"]
#exp
CoreServer_createActivity_01.code = APP_a["error_code_correct"]
#2.8.2
CoreServer_activityList_01 = activityList()
CoreServer_activityList_01.url = Shop_url +"/biz/projectActivity/activityList"
CoreServer_activityList_01.X_Type = APP_a["X-Type"]
CoreServer_activityList_01.shopId = APP_a["mendianId"]
CoreServer_activityList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_activityList_01.code = APP_a["error_code_correct"]
#2.8.3
CoreServer_activityDetail_01 = activityDetail()
CoreServer_activityDetail_01.url = Shop_url +"/biz/projectActivity/activityDetail"
CoreServer_activityDetail_01.activityId = APP_a["activityId"]
CoreServer_activityDetail_01.shopId = APP_a["mendianId"]
CoreServer_activityDetail_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_activityDetail_01.code = APP_a["error_code_correct"]
#2.8.4
CoreServer_activityQr_01 = activityQr()
CoreServer_activityQr_01.url = Shop_url +"/biz/projectActivity/activityQr"
CoreServer_activityQr_01.X_Type = APP_a["X-Type"]
CoreServer_activityQr_01.shopId = APP_a["mendianId"]
CoreServer_activityQr_01.activityId = APP_a["activityId"]
#exp
CoreServer_activityQr_01.code = APP_a["error_code_correct"]
#2.8.5
CoreServer_activityPersonnelList_01 = activityPersonnelList()
CoreServer_activityPersonnelList_01.url = Shop_url+"/biz/projectActivity/activityPersonnelList"
CoreServer_activityPersonnelList_01.X_Type = APP_a["X-Type"]
CoreServer_activityPersonnelList_01.activityId = APP_a["activityId"]
CoreServer_activityPersonnelList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_personnelDetails_01.code = APP_a["error_code_correct"]
#2.8.6
CoreServer_activityChooseProjectList_01 = activityChooseProjectList()
CoreServer_activityChooseProjectList_01.url = Shop_url +"/biz/projectActivity/activityChooseProjectList"
CoreServer_activityChooseProjectList_01.X_Type = APP_a["X-Type"]
CoreServer_activityChooseProjectList_01.shopId = APP_a["mendianId"]
CoreServer_activityChooseProjectList_01.pageSize = APP_a["pageSize"]
#exp
CoreServer_activityChooseProjectList_01.code = APP_a["error_code_correct"]