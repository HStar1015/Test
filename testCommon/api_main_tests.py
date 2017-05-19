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
    #5.6
    def test0006_getShareUrl_test(self):
        print "**********************************#5.6获取分享地址*******************************************"
        auth = apimsg.CoreServer_getShareUrl_01
        self.test.test_getShareUrl(auth)
        print "******************************************************************************************"
    #5.7
    def test0007_findPassword_test(self):
        print "**********************************#5.7 找回密码*******************************************"
        auth = apimsg.CoreServer_findPassword_01
        self.test.test_findPassword(auth)
        print "******************************************************************************************"
    #5.8
    def test0008_updatePassword_test(self):
        print "**********************************#5.8修改密码*******************************************"
        auth = apimsg.CoreServer_updatePassword_01
        self.test.test_updatePassword(auth)
        print "******************************************************************************************"
    #5.9
    def test0009_payMode_test(self):
        print "**********************************#5.9 获取支付方式*******************************************"
        auth = apimsg.CoreServer_payMode_01
        self.test.test_payMode(auth)
        print "******************************************************************************************"
    #5.10
    def test0010_areaList_test(self):
        print "**********************************#5.10 获取城市地区列表*******************************************"
        auth = apimsg.CoreServer_areaList_01
        self.test.test_areaList(auth)
        print "******************************************************************************************"
    #5.11
    def test0011_activityDetail_test(self):
        print "**********************************#5.11 获取活动详情*******************************************"
        auth = apimsg.CoreServer_activityDetail_01
        self.test.test_activityDetail(auth)
        print "******************************************************************************************"
    #5.12
    def test_vote_test(self):
        print "**********************************#5.12活动投票*******************************************"
        auth = apimsg.CoreServer_vote_01
        self.test.test_vote(auth)
        print "******************************************************************************************"
    #5.13
    def test_voteStatical_test(self):
        print "**********************************#5.13活动投票统计结果*******************************************"
        auth = apimsg.CoreServer_voteStatical_01
        self.test.test_voteStatical(auth)
        print "******************************************************************************************"
    #5.14
    def test_winList_test(self):
        print "**********************************#5.14中奖人名单*******************************************"
        auth = apimsg.CoreServer_winList_01
        self.test.test_winList(auth)
        print "******************************************************************************************"
    #5.15
    def test_peopleVoteStatus_test(self):
        print "**********************************#5.15 用户投票状态*******************************************"
        auth = apimsg.CoreServer_peopleVoteStatus_01
        self.test.test_peopleVoteStatus(auth)
        print "******************************************************************************************"
    #5.16
    def test_peopleVoteStatus_test(self):
        print "**********************************#5.16 获取项目图片库*******************************************"
        auth = apimsg.CoreServer_projectPhoto_01
        self.test.test_projectPhoto(auth)
        print "******************************************************************************************"
    #5.16
    def test_baiduCoordinate_test(self):
        print "**********************************#5.17 获取百度地图坐标信息*******************************************"
        auth = apimsg.CoreServer_baiduCoordinate_01
        self.test.test_baiduCoordinate(auth)
        print "******************************************************************************************"
