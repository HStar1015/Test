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
    #4.1.1注册
    def test0001_regist_test(self):
        print "**********************************#4.1.1注册**************************************************"
        auth = apimsg.CoreServer_register_01
        self.test.test_register_test(auth)
        print "**********************************************************************************************"
    #4.1.2
    def test0002_login_test(self):
        print "**********************************#4.1.2登录**************************************************"
        auth = apimsg.CoreServer_login_01
        self.test.test_login_test(auth)
        print "**********************************************************************************************"
    #4.1.3
    def test0003_updateInfo_test(self):
        print "**********************************#4.1.3修改顾客信息**************************************************"
        auth = apimsg.CoreServer_updateInfo_01
        self.test.test_updateInfo_test(auth)
        print "**********************************************************************************************"
    #4.1.4
    def test0004_customerInfo_test(self):
        print "**********************************#4.1.4获取顾客信息**************************************************"
        auth = apimsg.CoreServer_customerInfo_01
        self.test.test_customerInfo_test(auth)
        print "**********************************************************************************************"
    #4.1.5
    def test0005_collectProject_test(self):
        print "**********************************#4.1.5 收藏项目**************************************************"
        auth = apimsg.CoreServer_collectProject_01
        self.test.test_collectProject_test(auth)
        print "**********************************************************************************************"
    #4.1.6
    def test0006_collectProjectList_test(self):
        print "**********************************#4.1.6收藏项目列表**************************************************"
        auth = apimsg.CoreServer_collectProjectList_01
        self.test.test_collectProjectList_test(auth)
        print "**********************************************************************************************"
    #4.1.7
    def test0007_collectPersonnel_test(self):
        print "**********************************#4.1.7收藏美容师**************************************************"
        auth = apimsg.CoreServer_collectPersonnel_01
        self.test.test_collectPersonnel_test(auth)
        print "**********************************************************************************************"
    #4.1.8
    def test0008_collectPersonneList_test(self):
        print "**********************************#4.1.8收藏美容师列表**************************************************"
        auth = apimsg.CoreServer_collectPersonnelList_01
        self.test.test_collectPersonneList_test(auth)
        print "**********************************************************************************************"
    #4.1.9
    def test0009_miniAppLogin_test(self):
        print "**********************************#4.1.9 小程序授权用户查询**************************************************"
        auth = apimsg.CoreServer_miniAppLogin_01
        self.test.test_miniAppLogin_test(auth)
        print "**********************************************************************************************"
    #4.2.1
    def test0010_projectPersonnelList_test(self):
        print "**********************************#4.2.1 获取参与项目的美容师列表**************************************************"
        auth = apimsg.CoreServer_projectPersonnelList_01
        self.test.test_projectPersonnelList_test(auth)
        print "**********************************************************************************************"
    #4.2.2
    def test0011_personnelProjectList_test(self):
        print "**********************************#4.2.2获取美容师参与的项目列表**************************************************"
        auth = apimsg.CoreServer_personnelProjectList_01
        self.test.test_personnelProjectList_test(auth)
        print "**********************************************************************************************"
    #4.2.3
    def test0012_orderSave_test(self):
        print "**********************************#4.2.2预约项目提交**************************************************"
        auth = apimsg.CoreServer_orderSave_01
        self.test.test_orderSave_test(auth)
        print "**********************************************************************************************"