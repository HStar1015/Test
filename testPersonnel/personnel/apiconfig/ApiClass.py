# -*- coding: utf-8 -*-
#************************3.1*******************************
#3.1.1注册
class register:
    '''request'''
    url=""
    phone = ""
    password = ""
    authCode = ""
    X_Type= ""
    #expect
    code = ""

#3.1.2登录
class login:
    '''request'''
    url = ""
    phone = ""
    password = ""
    X_Type= ""
    #expect
    code = ""
#3.1.3
class acceptInvitation:
    url=""
    X_Type = ""
    id = ""
    businessId = ""
    shopId = ""
    #exp
    code = ""
#3.1.4
class personnelInfo:
    url= ""
    X_Type =""
    id = ""
    #exp
    code = ""
#3.1.5
class updateInfo:
    url = ""
    X_Type = ""
    id = ""
    name =""
    sex = ""
    files =""
    #description = ""
    #exp
    code = ""
class worlTime:
    id =""
    monStart =""
    monEnd=""
    tueStart=""
    tueEnd=""
    wedStart=""
    wedEnd=""
    thuStart=""
    thuEnd=""
    friStart=""
    friEnd=""
    satStart=""
    satEnd=""
    sunStart=""
    sunEnd=""
    ifMonWork=""
    ifTueWork=""
    ifWedWork=""
    ifThuWork=""
    ifFriWork=""
    ifSatWork=""
    ifSunWork=""

    X_Type = ""
    #exp
    code = ""
#3.1.7
class getWorkTime:
    url = ""
    X_Type = ""
    personnelId= ""
    #exp
    code= ""
#3.1.8
class shopInfo:
    url = ""
    X_Type = ""
    shopId = ""
    #exp
    code = ""
#3.1.9
class updateRegistrationId:
    url = ""
    X_Type = ""
    id = ""
    registrationId = ""
    #exp
    code = ""
#********************************3.2******************************************
#3.2.1
class projectList:
    url= ""
    X_Type = ""
    shopId = ""
    personnelId = ""
    pageSize = ""
    #exp
    code  = ""
#3.2.2
class chooseProject:
    url = ""
    X_Type = ""
    projectIds = ""
    personnelId = ""
    #exp
    code = ""
#3.2.3
class myProjectList:
    url = ""
    X_Type = ""
    shopId = ""
    personnelId= ""
    pageSize = ""
    #exp
    code  = ""
#3.2.4
class delProject:
    url = ""
    X_Type =""
    projectIds = ""
    personnelId = ""
    #exp
    code = ""
#3.2.5
class projectDetails:
    url = ""
    X_Type= ""
    id = ""
    #exp
    code = ""
#**************************************3.3****************************
#3.3.1
class orderGroupNum:
    url = ""
    X_Type = ""
    shopId = ""
    personnelId = ""
    #exp
    code = ""
#3.3.2
class myOrderList:
    url= ""
    X_Type = ""
    shopId = ""
    personnelId = ""
    pageSize = ""
    #exp
    code=""
#3.3.3
class orderDetail:
    url = ""
    X_Type =""
    personnelId = ""
    orderNo = ""
    #exp
    code =""
#3.3.4
class cancelOrder:
    url = ""
    X_Type = ""
    personnelId = ""
    orderNo = ""
    #exp
    code = ""
#3.3.5
class confirmFinishOrder:
    url = ""
    X_Type = ""
    personnelId = ""
    orderNo = ""
    #exp
    code = ""
#3.3.6
class scanFinishOrder:
    url = ""
    X_Type = ""
    personnelId =""
    payCode =""
    #exp
    code = ""
#3.3.7
class orderSave:
    url = ""
    X_Type = ""
    projectId =  ""
    personnelId =""
    makeStartDate = ""
    makeEndDate = ""
    priceType = ""
    reserveName = ""
    reservePhone = ""
    #exp
    code = ""
#***************************************************3.4*****************************************
#3.4.1
class customerList:
    url = ""
    X_Type = ""
    shopId =""
    personnelId = ""
    pageSize = ""
    #exp
    code = ""
#3.4.2
class changeRemark:
    url = ""
    X_Type =""
    shopId = ""
    personnelId = ""
    remark = ""
    customerId = ""
    #exp
    code=""
#3.4.3
class changeRank:
    url = ""
    X_Type = ""
    shopId = ""
    rankId = ""
    customerIds = ""
    #exp
    code = ""
#3.4.4
class customerDetails:
    url = ""
    X_Type = ""
    shopId = ""
    customerId = ""
    #exp
    code = ""
#3.4.5
class expenseRecord:
    url = ""
    X_Type = ""
    customerId = ""
    shopId = ""
    pageSize = ""
    #exp
    code = ""
#3.4.6
class expenseProject:
    url = ""
    X_Type = ""
    customerId  =""
    shopId = ""
    pageSize = ""
    #exp
    code = ""
#3.4.7
class rankInfoList:
    url = ""
    X_Type = ""
    shopId = ""
    personnelId = ""

    #exp
    code = ""

#3.4.8.1
class createCard:
    url = ""
    X_Type = ""
    shopId = ""
    personnelId =""
    customerId = ""
    cardType = ""
    name = ""
    remark = ""
    validityDate = ""
    #exp
    code = ""
# 3.4.8.2
class editCard:
    url = ""
    X_Type =""
    shopId = ""
    personnelId = ""
    customerId = ""
    cardType = ""
    id = ""
    name = ""
    remark = ""
    validityDate = ""
    # totalNum =""
    # surplusNum =""
    #exp
    code = ""
# 3.4.8.3
class cardDetail:
    url = ""
    X_Type = ""
    cardId = ""
    #exp
    code = ""
# 3.4.8.4
class customerCardList:
    url = ""
    X_Type=""
    shopId = ""
    customerId = ""
    pageSize = ""
    page = ""
    #exp
    code = ""
# 3.4.8.5
class operationCard:
    url = ""
    X_Type =""
    shopId = ""
    personnelId = ""
    customerId =""
    cardType = ""
    id = ""
    deductNum = ""
    #exp
    code = ""
# 3.4.8.6
class cardConsummerDetailList:
    url = ""
    X_Type = ""
    cardId = ""
    pageSize =""
    # exp
    code = ""
#*****************************************************3.5*********************************************
#3.5.1
class commentGroupNum:
    url = ""
    X_Type =""
    personnelId = ""
    #exp
    code = ""
#3.5.2
class commentList:
    url = ""
    X_Type = ""
    personnelId =""
    commentLevel =""
    pageSize = ""
    #exp
    code = ""
#******************************************************3.6********************************************
#3.6.1
class activityList:
    url = ""
    X_Type = ""
    shopId = ""
    pageSize =""
    #exp
    code = ""
#3.6.2
class activityDetail:
    url = ""
    X_Type = ""
    activityId = ""
    shopId = ""
    pageSize = ""
    #exp
    code = ""
#3.6.3
class activityQr:
    url = ""
    X_Type = ""
    shopId = ""
    activityId = ""
    personnelId = ""
    #exp
    code = ""
#******************************2017-3-29新增接口---工作计划总结相关**************************
#**************************************************3.7***************************************
#3.7.1
class createPlan:
    url = ""
    X_Type = ""
    month = ""
    personnelId = ""
    personnelPlanDetailDtos =""
    customerRankId = ""
    planPerformance = ""
    planIntroduce = ""
    #exp
    code = ""
#3.7.2
class editPlan:
    url = ""
    X_Type = ""
    id =""
    personnelPlanDetailDtos = ""
    customerRankId = ""
    planPerformance = ""
    planIntroduce = ""
    #exp
    code= ""
#3.7.3
class selectPlanDetail:
    url = ""
    X_Type =""
    planId = ""
    #exp
    code = ""
#3.7.4
class selectCustomerList:
    url = ""
    X_Type = ""
    shopId = ""
    personnelId= ""
    operationType = ""
    recordType =""
    customerType = ""
    #exp
    code = ""
#3.7.5
class selectPlanList:
    url=""
    X_Type = ""
    personnelId= ""
    #exp
    code = ""
#3.7.6
class createDaySummarize:
    url = ""
    X_Type = ""
    personnelId = ""
    day = ""
    dayPerformance = ""
    dayExpend = ""
    dayOrder =""
    newExperienceIntroduce = ""
    newExperienceDevelop = ""
    newTransactionIntroduce = ""
    newTransactionDevelop = ""
    summary =""
    performanceList=""
    customerRankId=""
    planPerformance=""
    custmerType=""
    expendList=""
    customerRankId=""
    planPerformance=""
    #exp
    code = ""
#3.7.9
class editDaySummarize:
    url = ""
    X_Type = ""
    planId = ""
    id =""
    day = ""
    dayPerformance = ""
    dayExpend = ""
    dayOrder = ""
    newExperienceIntroduce = ""
    newExperienceDevelop = ""
    newTransactionIntroduce = ""
    newTransactionDevelop = ""
    summary = ""
    performanceList = ""
    customerRankId = ""
    planPerformance = ""
    custmerType = ""
    expendList = ""
    customerRankId = ""
    planPerformance = ""
    # exp
    code = ""
#3.7.8
class selectDaySummarizeDetail:
    url =""
    X_Type = ""
    summarizeId = ""
    #exp
    code = ""
#3.7.9
class selectSummarizeList:
    url = ""
    X_Type =""
    planId =""
    #exp
    code = ""



