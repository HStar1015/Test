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