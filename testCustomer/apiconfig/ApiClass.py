# -*- coding: utf-8 -*-
#************************4.1*******************************
#4.1.1注册
class register:
    '''request'''
    url=""
    phone = ""
    password = ""
    authCode = ""
    X_Type= ""
    #expect
    code = ""
#4.1.2登录
class login:
    '''request'''
    url = ""
    phone = ""
    password = ""
    X_Type= ""
    #expect
    code = ""
#4.1.3
class updateInfo:
    id = ""
    X_Type = ""
    url = ""
    files = ""
    #exp
    code= ""
#4.1.4
class cutomerInfo:
    id =""
    X_Type = ""
    url = ""
    #exp
    code = ""
#4.1.5
class collectProject:
    url = ""
    X_Type = ""
    customerId = ""
    projectId = ""
    ifCollect  = ""
    #exp
    code = ""
#4.1.6
class collectProjectList:
    url= ""
    X_Type = ""
    customerId = ""
    longitude = ""
    latitude = ""
    pageSize = ""
    #exp
    code = ""
#4.1.7
class collectPersonnel:
    url = ""
    X_Type = ""
    customerId = ""
    personnelId = ""
    ifCollect = ""
    #exp
    code= ""
#4.1.8
class collectPersonnelList:
    url = ""
    X_Type = ""
    customerId = ""
    longitude = ""
    latitude = ""
    pageSize = ""
    #exp
    code= ""
#4.1.9
class miniAppLogin:
    url = ""
    X_Type = ""
    openId = ""
    #exp
    code = ""
#************************************4.2***********************************************
#4.2.1
class projectPersonnelList:
    url =""
    X_Type = ""
    projectId = ""
    pageSize = ""
    #exp
    code = ""
#4.2.2
class personnelProjectList:
    url =""
    X_Type = ""
    personnelId = ""
    pageSize = ""
    #exp
    code = ""
#4.2.3
class orderSave:
    url = ""
    X_Type = ""
    projectId = ""
    personnelId= ""
    customerId = ""
    makeStartDate = ""
    makeEndDate  = ""
    priceType = ""
    reserveName= ""
    reservePhone=""
    #exp
    code = ""
#4.2.4
class cancelOrder:
    url = ""
    X_Type =""
    orderNo = ""
    customerId = ""
    #exp
    code=""
#4.2.5
class applyCancelOrder:
    url = ""
    X_Type = ""
    orderNo = ""
    customerId = ""
    # exp
    code = ""
#4.2.6
class personnelServeProject:
    url = ""
    X_Type = ""
    projectId = ""
    personnelId = ""
    #exp
    code = ""
#*************************************4.3***************************************
#4.3.1.1
class hotProject:
    url = ""
    X_Type = ""
    longitude = ""
    latitude = ""
    cityId = ""
    pageSize = ""
    #exp
    code = ""
#4.3.1.2
class searchProjectList:
    url = ""
    X_Type = ""
    cityId = ""
    longitude = ""
    latitude = ""
    page = ""
    pageSize = ""
    #exp
    code = ""
#4.3.1.3
class projectDetails:
    url = ""
    X_Type = ""
    id = ""
    #exp
    code= ""
#4.3.1.4
class projectCommentGroupNum:
    url = ""
    X_Type = ""
    projectId = ""
    #exp
    code= ""
#4.3.1.5
class projectCommentList:
    url = ""
    X_Type =""
    projectId = ""
    commentLevel = ""
    pageSize = ""
    #exp
    code = ""

#4.3.2.1
class hotPersonnel:
    url = ""
    X_Type = ""
    longitude = ""
    latitude = ""
    cityId = ""
    pageSize = ""
    #exp
    code= ""
#4.3.2.2
class searchPersonnelList:
    url = ""
    X_Type = ""
    cityId = ""
    longitude = ""
    latitude = ""
    pageSize = ""
    #exp
    code = ""
#4.3.2.3
class personnelDetail:
    url = ""
    X_Type = ""
    id = ""
    #exp
    code = ""
#4.3.2.4
class personnelProjectList:
    url = ""
    X_Type = ""
    shopId = ""
    personnelId = ""
    pageSize = ""
    #exp
    code = ""
#4.3.2.5
class personnelCommentGroupNum:
    url = ""
    X_Type =""
    personnelId = ""
    #exp
    code = ""
#4.3.2.6
class personnelCommentList:
    url = ""
    X_Type = ""
    personnelId  =""
    commentLevel = ""
    pageSize = ""
    #exp
    code = ""
#****************************************4.4**********************************************
#4.4.1
class reserveProjectRecord:
    url = ""
    X_Type = ""
    customerId =""
    longitude = ""
    latitude =""
    pageSize = ""
    #exp
    code = ""
#4.4.2
class reservePersonnelRecord:
    url = ""
    X_Type = ""
    customerId =""
    longitude = ""
    latitude =""
    pageSize = ""
    #exp
    code = ""
#4.4.3
class orderGroupNum:
    url = ""
    X_Type =  ""
    customerId = ""
    #exp
    code = ""
#4.4.4
class myOrderList:
    url = ""
    X_Type =""
    customerId  =""
    approveStatus = ""
    pageSize = ""
    #exp
    code = ""
#4.4.5
class orderDetail:
    url = ""
    X_Type = ""
    customerId = ""
    orderNo = ""
    #exp
    code = ""
#4.4.6
class payQRDetail:
    url = ""
    X_Type =""
    customerId = ""
    orderNo = ""
    #exp
    code = ""
#4.4.7
class orderComment:
    url = ""
    X_Type= ""
    orderNo = ""
    customerId =""
    personnelId =""
    projectId =""
    content= ""
    domainLevel =""
    serveLevel =""
    communicationLevel =""
    #exp
    code = ""
#4.4.7
class confirmFinishOrder:
    url = ""
    X_Type = ""
    personnelId  = ""
    orderNo = ""
    #exp
    code = ""
#************************4.5*********************
#4.5.1
class wechatSubmitPay:
    url = ""
    X_Type =""
    openId = ""
    customerId= ""
    orderNo = ""
    paymentMode = ""
    #exp
    code = ""
#4.5.2
class appSubmitPay:
    url = ""
    X_Type = ""
    customerId = ""
    orderNo = ""
    paymentMode = ""
    # exp
    code = ""
#4.5.3
class checkOrderPayStatus:
    url = ""
    X_Type = ""
    customerId = ""
    orderNo = ""
    #exp
    code = ""