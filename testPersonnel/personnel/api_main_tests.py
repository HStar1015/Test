# -*- coding: utf-8 -*-
import unittest
from lib import actions
from lib import modules
import apiconfig.ProductionEnv_config as apimsg
import datetime

class core_server_tests(unittest.TestCase):
    test = modules.test_core_server()
    def setUp(self):
        currentTime = str(datetime.datetime.now())[0:19]
        print "@@@@@@@@@@-- RUN TESTCASE --%s@@@@@@@@@@" % currentTime
        pass

    def tearDown(self):
        pass
    #3.1.1注册
    def test0001_regist_test(self):
        print "**********************************#3.1.1注册**************************************************"
        auth = apimsg.CoreServer_register_01
        self.test.test_register_test(auth)
        print "**********************************************************************************************"
    #3.1.2
    def test0002_login_test(self):
        print "**********************************#3.1.2登录**************************************************"
        auth = apimsg.CoreServer_login_01
        self.test.test_login_test(auth)
        print "**********************************************************************************************"
    #3.1.3
    def test0003_acceptInvitation_test(self):
        print "**********************************#3.1.3接受邀请**************************************************"
        auth = apimsg.CoreServer_acceptInvitation_01
        self.test.test_acceptInvitation_test(auth)
        print "**********************************************************************************************"
    #3.1.4
    def test0004_personnelInfo_test(self):
        print "**********************************#3.1.4获取员工信息**************************************************"
        auth = apimsg.CoreServer_personnelInfo_01
        self.test.test_personnelInfo_test(auth)
        print "**********************************************************************************************"
    #3.1.5
    def test0005_updateInfo_test(self):
        print "**********************************#3.1.5修改员工信息**************************************************"
        auth = apimsg.CoreServer_updateInfo_01
        self.test.test_updateInfo(auth)
        print "**********************************************************************************************"
    #3.1.6
    def test0006_workTime_test(self):
        print "**********************************#3.1.6设置工作时间**************************************************"
        auth = apimsg.CoreServer_workTime
        self.test.test_workTime(auth)
        print "**********************************************************************************************"
    #3.1.7
    def test0007_getWorkTime_test(self):
        print "**********************************#3.1.7查询工作时间**************************************************"
        auth = apimsg.CoreServer_getWorkTime_01
        self.test.test_getWorkTime(auth)
        print "**********************************************************************************************"
    #3.1.8
    def test0008_shopInfo_test(self):
        print "**********************************#3.1.8获取所属门店信息**************************************************"
        auth = apimsg.CoreServer_shopInfo_01
        self.test.test_shopInfo(auth)
        print "**********************************************************************************************"
    #3.1.9
    def test0009_updateRegistrationId(self):
        print "**********************************#3.1.9更新用户设备id**************************************************"
        auth = apimsg.CoreServer_updateRegistrationId_01
        self.test.test_updateRegistration(auth)
        print "**********************************************************************************************"
    #3.2.1
    def test0010_projectList(self):
        print "**********************************#3.2.1获取门店项目列表**************************************************"
        auth = apimsg.CoreServer_projectList_01
        self.test.test_projectList(auth)
        print "**********************************************************************************************"