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
