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
    #5.1
    def test0001_authPhone_test(self):
        print "**********************************#5.1发送验证码*******************************************"
        auth = apimsg.CoreServer_authPhone_01
        self.test.test_authPhone(auth)
        print "******************************************************************************************"
    #5.2
    def test0002_authPic_test(self):
        print "**********************************#5.2获取图片验证码*******************************************"
        auth = apimsg.CoreServer_authPic_01
        self.test.test_authPic(auth)
        print "******************************************************************************************"
    #5.3
    def test0003_projectTypeTree_test(self):
        print "**********************************#5.3获取项目类别*******************************************"
        auth = apimsg.CoreServer_projectTypeTree_01
        self.test.test_projectTypeTree(auth)
        print "******************************************************************************************"
    #5.4
    def test0004_message_test(self):
        print "**********************************#5.4优美消息*******************************************"
        auth = apimsg.CoreServer_message_01
        self.test.test_message(auth)
        print "******************************************************************************************"
    #5.5
    def test0005_rankList_test(self):
        print "**********************************#5.5 获取分组列表*******************************************"
        auth = apimsg.CoreServer_rankList_01
        self.test.test_rankList(auth)
        print "******************************************************************************************"

