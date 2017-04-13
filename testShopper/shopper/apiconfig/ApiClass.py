# -*- coding: utf-8 -*-
#************************2.1*******************************
#2.1.1注册
class register:
    '''request'''
    url=""
    phone = ""
    password = ""
    authCode = ""
    inviteCode = ""
    X_Type= ""
    #expect
    code = ""

#2.1.2登录
class login:
    '''request'''
    url = ""
    phone = ""
    password = ""
    X_Type= ""

    #expect
    code = ""
    shop_id =""
    shop_name =""
    shop_phone= ""
    shop_header = ""
    token = ""
    alias = ""
    inviteStatus = ""

#2.1.3申请邀请码
class applyInvite:
    url = ""
    phone = ""
    name = ""
    provinceId = ""
    cityId = ""
    areaId = ""
    X_Type =""
    #expect
    code = ""

#2.1.4修改商家信息
class updateInfo:
    url = ""
    id = ""
    X_Type =""
    #exp
    code = ""
#2.1.5获取商家信息
class businessInfo:
    id = ""
    url = ""
    X_Type =""
    #exp
    code = ""
#2.1.6更新用户设备ID
class updateRegistrationId:
    id = ""
    registrationId = ""
    url = ""
    X_Type = ""
    #exp
    code = ""
#************************2.2*******************************
#2.2.1
class saveShop:
    businessId = ""
    phone = ""
    shopName = ""
    shortName = ""
    description =""
    provinceId = ""
    cityId = ""
    areaId = ""
    address = ""
    url = ""
    X_Type =""
    files =""
    #exp
    code = ""
#2.2.2
class updateInfo:
    businessId = ""
    phone = ""
    shopName = ""
    shortName = ""
    description = ""
    provinceId = ""
    cityId = ""
    areaId = ""
    address = ""
    url = ""
    X_Type = ""
    files = ""
    # exp
    code = ""
#2.2.3
class shopList:
    '''req'''
    businessId = ""
    auth = ""
    X_Type = ""
    url = ""
    #exp
    code = ""
#2.2.4
class shopInfo:
    '''req'''
    id = ""
    X_Type= ""
    url = ""
    #exp
    code = ""
#2.2.5
class deleteShop:
    '''req'''
    id = ""
    businessId = ""
    url = ""
    X_Type = ""
    #exp
    code = ""
#************************2017-04-12-新增接口--2.2.6店数据统计**************************
#2.2.6.1
class shopStatics:
    url = ""
    X_Type = ""
    shopId = ""
    month = ""
    #exp
    code = ""
#2.2.6.2
class saleStatistics:
    url = ""
    X_Type = ""
    shopId = ""
    month = ""
    #exp
    code = ""
#2.2.6.3
class newCustomerStatistics:
    url = ""
    X_Type = ""
    shopId = ""
    month = ""
    #exp
    code = ""
#2.2.6.4
class projectSaleStatistics:
    url = ""
    X_Type = ""
    shopId = ""
    month = ""
    #exp
    code = ""
#************************2.3*******************************
#2.3.1
class addProject:
    businessId = ""
    url = ""
    X_Type = ""
    shopIds = ""
    projectName =""
    groupNo =""
    unitPrice = ""
    coursePrice = ""
    courseRemark = ""
    duration= ""
    description=""
    applyPerson =""
    brand =""
    noticeMatters = ""
    files = ""
    #exp
    code = ""
#2.3.2
class deleteProject:
    id = ""
    url= ""
    X_Type= ""
    #exp
    code= ""
#2.3.3
class editProject:
    id = ""
    url = ""
    X_Type = ""
    projectName = ""
    groupNo = ""
    unitPrice = ""
    coursePrice = ""
    courseRemark = ""
    duration = ""
    description = ""
    applyPerson = ""
    brand = ""
    noticeMatters = ""
    files = ""
    fileUuid =""
    picCount=""
    # exp
    code = ""
#2.3.4
class projectList:
    url = ""
    X_Type = ""
    shopId = ""
    pageSize = ""
    #exp
    code= ""
#2.3.5
class projectDetails :
    url =""
    X_Type =""
    id= ""
    #exp
    code=""
#2.3.6
class copyProject:
    url = ""
    X_Type = ""
    businessId = ""
    shopId =""
    projectIds= ""
    #exp
    code = ""
#************************2.4*******************************
#2.4.1
class pushInvitation:
    personnelPhone =""
    businessId = ""
    shopId  =""
    phone = ""
    url = ""
    X_Type = ""
    #exp
    code =""
#2.4.2
class personnelList:
    url = ""
    X_Type =""
    businessId = ""
    shopId = ""
    pageSize = ""
    #exp
    code =""
#2.4.3
class personnelDetails:
    url = ""
    X_Type= ""
    id = ""
    #exp
    code= ""
#2.4.4
class unbind:
    url = ""
    X_Type = ""
    id = ""
    businessId = ""
    #exp
    code = ""
#2.4.5
class allocationPersonnel:
    businessId =""
    shopId = ""
    personnelIds = ""
    url = ""
    X_Type = ""
    #exp
    code =""
#2.4.6.1
class commentGroupNum:
    url = ""
    X_Type= ""
    personnelId =""
    #exp
    code=""
#2.4.6.2
class commentList:
    url = ""
    X_Type =""
    personnelId = ""
    commentLevel =""
    pageSize = ""
    #exp
    code =""
#2.4.7.1
class daySummarizeList:
    url= ""
    X_Type = ""
    day = ""
    shopId = ""
    pageSize=""
    #exp
    code = ""
#2.4.7.2
class daySummarizeDetail:
    url = ""
    X_Type = ""
    summarizeId = ""
    #exp
    code = ""
#2.4.7.3
class monthPlanList:
    url= ""
    X_Type = ""
    month = ""
    shopId =""
    pageSize = ""
    #exp
    code = ""
#2.4.7.4
class monthPlanDetail:
    url = ""
    X_Type =""
    planId = ""
    #exp
    code = ""
#2.4.8.2
class operationCaseList:
    shopId = ""
    url = ""
    X_Type=""
    #exp
    code = ""
#2.4.8.2
class operationCaseDetail:
    shopId=""
    month=""
    url = ""
    X_Type = ""
    #exp
    code = ""
#************************2.5*******************************
#2.5.1
class customerList:
    url = ""
    X_Type = ""
    shopId = ""
    pageSize =""
    #exp
    code=""
#2.5.2
class customerDetails:
    url = ""
    X_Type = ""
    shopId = ""
    customerId = ""
    #exp
    code = ""
#2.5.3
class allocationCustomer:
    url = ""
    X_Type  =""
    shopId = ""
    personnelId = ""
    customerId = ""
    #exp
    code = ""
#2.5.4
class expenseRecord:
    url = ""
    X_Type = ""
    customerId = ""
    shopId = ""
    pageSize= ""
    #exp
    code = ""
#2.5.5
class expenseProject:
    url= ""
    X_Type= ""
    customerId = ""
    shopId = ""
    pageSize = ""
    # exp
    code = ""
#2.5.6
class changeRank:
    url = ""
    X_Type = ""
    shopId =""
    rankId = ""
    customerIds = ""
    #exp
    code = ""
#2.5.7
class rankInfoList:
    url = ""
    X_Type = ""
    shopId = ""
    #exp
    code = ""
#2.5.8.1
class customerCardList:
    url = ""
    X_Type = ""
    shopId =""
    customerId = ""
    pageSize = ""
    #exp
    code= ""
#2.5.8.2
class cardConsummerDetailList:
    url = ""
    X_Type = ""
    cardId = ""
    pageSize = ""
    # exp
    code = ""
#*****************************************2.6*****************************************
#2.6.1
class findAccountBalance:
    url = ""
    X_Type= ""
    businessId=""
    #exp
    code = ""
#2.6.2
class accountRecordList:
    url =""
    X_Type=""
    businessId = ""
    pageSize = ""
    #exp
    code = ""
#2.6.3
class putApply:
    url= ""
    X_Type= ""
    businessId = ""
    paymentMode = ""
    price =""
    #exp
    code = ""
#2.6.4
class putRecordDetail:
    url= ""
    X_Type= ""
    id =""
    #exp
    code = ""
#2.6.5
class incomeRecordDetail:
    url= ""
    id = ""
    X_Type = ""
    #exp
    code= ""
#**********************************************2.7*****************************************
#2.7.1
class shopCapacity:
    url = ""
    X_Type = ""
    businessId = ""
    shopId = ""
    bunkCount =""
    projectAverageDuration =""
    workStartDate = ""
    workEndDate = ""
    personnelCount = ""
    customerAverageExpense = ""
    activeCustomerCount = ""
    mainProjectAverageDuration = ""
    #exp
    code = ""
#2.7.2
class shopDiagnose:
    url = ""
    X_Type = ""
    businessId = ""
    shopId = ""
    monthShopTurnover =""
    dayShopCustomerCount =""
    personnelCount=""
    monthTookeenCount=""
    yearShopTurnover=""
    #exp
    code =""
#2.7.3
class getShopCapacity:
    url = ""
    X_Type = ""
    businessId = ""
    shopId = ""
    #exp
    code = ""
#2.7.4
class getShopDiagnose:
    url = ""
    X_Type =""
    businessId= ""
    shopId = ""
    #exp
    code = ""
#************************************2.8*******************************
#2.8.1
class createActivity:
    url = ""
    businessId=""
    shopId = ""
    activityName = ""
    activityStartDate = ""
    activityEndDate = ""
    activityUnitPrice = ""
    activityCoursePrice = ""
    description = ""
    projectIds = ""
    X_Type = ""
    #exp
    code = ""
#2.8.2
class activityList:
    url = ""
    X_Type = ""
    shopId = ""
    pageSize = ""
    #exp
    code = ""
#2.8.3
class activityDetail:
    url = ""
    X_Type = ""
    activityId = ""
    shopId = ""
    pageSize = ""
    #exp
    code = ""
#2.8.4
class activityQr:
    url = ""
    X_Type =""
    shopId =""
    activityId = ""
    #exp
    code = ""
#2.8.5
class activityPersonnelList:
    url = ""
    X_Type = ""
    activityId = ""
    pageSize = ""
    #exp
    code = ""
#2.8.6
class activityChooseProjectList:
    url = ""
    X_Type = ""
    shopId = ""
    pageSize =""
    #exp
    code = ""