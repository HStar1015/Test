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
    "files":"",
    "pageSize":100,
    "projectId":"216",
    "orderNo":"DD7312548808254750113",#订单编号
    "payCode":"QR7543166741178590773",#支付码
    "makeStartDate":"2017-03-28 12:00:00",#预约开始时间
    "makeEndDate":"2017-03-28 12:30:00",#预约结束时间
    "priceType":1,#价格类型,0(单价)/1(疗程)
    "reserveName":"xing",
    "reservePhone":"13051175683",
    "customerId":43,#顾客id
    "remark":"hello",
    "rankId":1,
    "activityId":163,

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
CoreServer_register_01.inviteCode = "QWERTYU"
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

