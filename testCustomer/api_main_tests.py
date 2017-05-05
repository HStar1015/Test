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
    # #4.1.9
    # def test0009_miniAppLogin_test(self):
    #     print "**********************************#4.1.9 小程序授权用户查询**************************************************"
    #     auth = apimsg.CoreServer_miniAppLogin_01
    #     self.test.test_miniAppLogin_test(auth)
    #     print "**********************************************************************************************"
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
     #4.2.4
    def test0013_cancelOrder_test(self):
        print "**********************************#4.2.4 取消预约**************************************************"
        auth = apimsg.CoreServer_cancelOrder_01
        self.test.test_cancelOrder_test(auth)
        print "**********************************************************************************************"
    #4.2.5
    def test0014_applyCancelOrder_test(self):
        print "**********************************#4.2.5申请取消预约**************************************************"
        auth = apimsg.CoreServer_applyCancelOrder_01
        self.test.test_applyCancelOrder_test(auth)
        print "**********************************************************************************************"
    #4.2.6
    def test0015_personnelServeProject_test(self):
        print "**********************************#4.2.6 判断美容师是否还服务项目**************************************************"
        auth = apimsg.CoreServer_personnelServeProject_01
        self.test.test_personnelServeProject_test(auth)
        print "**********************************************************************************************"
    #4.3.1.1
    def test0015_personnelServeProject_test(self):
        print "**********************************#4.3.1.1 热门项目**************************************************"
        auth = apimsg.CoreServer_hotProject_01
        self.test.test_hotProject_test(auth)
        print "**********************************************************************************************"
    #4.3.1.2
    def test0016_searchProjectList_test(self):
        print "**********************************#4.3.1.2 搜索项目列表**************************************************"
        auth = apimsg.CoreServer_searchProjectList_01
        self.test.test_searchProjectList_test(auth)
        print "**********************************************************************************************"
    #4.3.1.3
    def test0017_projectDetails_test(self):
        print "**********************************#4.3.1.3 项目详情**************************************************"
        auth = apimsg.CoreServer_projectDetails_01
        self.test.test_projectDetails_test(auth)
        print "**********************************************************************************************"
    #4.3.1.4
    def test0018_projectCommentGroupNum_test(self):
        print "**********************************#4.3.1.4 项目评论分组数量**************************************************"
        auth = apimsg.CoreServer_projectCommentGroupNum_01
        self.test.test_projectCommentGroupNum_test(auth)
        print "**********************************************************************************************"
    #4.3.1.5
    def test0019_projectCommentList_test(self):
        print "**********************************#4.3.1.5 项目评论列表**************************************************"
        auth = apimsg.CoreServer_projectCommentList_01
        self.test.test_projectCommentList_test(auth)
        print "**********************************************************************************************"
    #4.3.2.1
    def test0020_hotPersonnel_test(self):
        print "**********************************#4.3.2.1 热门美容师**************************************************"
        auth = apimsg.CoreServer_hotPersonnel_01
        self.test.test_hotPersonnel_test(auth)
        print "**********************************************************************************************"
    #4.3.2.2
    def test0021_searchPersonnelList_test(self):
        print "**********************************#4.3.2.2 搜索美容师列表**************************************************"
        auth = apimsg.CoreServer_searchProjectList_01
        self.test.test_searchProjectList_test(auth)
        print "**********************************************************************************************"
    #4.3.2.3
    def test0022_personnelDetail_test(self):
        print "**********************************#4.3.2.3 美容师详情**************************************************"
        auth = apimsg.CoreServer_personnelDetail_01
        self.test.test_personnelDetail_test(auth)
        print "**********************************************************************************************"
    #4.3.2.4
    def test0023_personnelProjectList(self):
        print "**********************************#4.3.2.4 美容师项目列表**************************************************"
        auth = apimsg.CoreServer_personnelProjectList_01
        self.test.test_personnelProjectList_test(auth)
        print "**********************************************************************************************"
    #4.3.2.5
    def test0023_personnelCommentGroupNum(self):
        print "**********************************#4.3.2.5 美容师评论分组数量**************************************************"
        auth = apimsg.CoreServer_personnelCommentGroupNum_01
        self.test.test_personnelCommentGroupNum_test(auth)
        print "**********************************************************************************************"
    #4.3.2.6
    def test0024_personnelCommentList(self):
        print "**********************************#4.3.2.6 美容师评论列表**************************************************"
        auth = apimsg.CoreServer_personnelCommentList_01
        self.test.test_personnelCommentList_test(auth)
        print "************************************************************"
    #4.4.1
    def test0025_reserveProjectRecord(self):
        print "**********************************#4.4.1 预约过的项目**************************************************"
        auth = apimsg.CoreServer_reserveProjectRecord_01
        self.test.test_reserveProjectRecord(auth)
        print "**********************************************************************************************"
    #4.4.2
    def test0026_reservePersonnelRecord(self):
        print "**********************************#4.4.2 预约过的美容师**************************************************"
        auth = apimsg.CoreServer_reservePersonnelRecord_01
        self.test.test_reservePersonnelRecord(auth)
        print "**********************************************************************************************"
    #4.4.3
    def test0027_orderGroupNum(self):
        print "**********************************#4.4.3 我的订单分组数量**************************************************"
        auth = apimsg.CoreServer_orderGroupNum_01
        self.test.test_orderGroupNum(auth)
        print "**********************************************************************************************"
    #4.4.4
    def test0028_myOderList(self):
        print "**********************************#4.4.4 我的订单列表**************************************************"
        auth = apimsg.CoreServer_myOderList_01
        self.test.test_myOrderList(auth)
        print "**********************************************************************************************"
    #4.4.5
    def test0029_orderDetail(self):
        print "**********************************#4.4.5 订单详情**************************************************"
        auth = apimsg.CoreServer_orderDetail_01
        self.test.test_orderDetail(auth)
        print "**********************************************************************************************"
    #4.4.6
    def test0030_payQRDetail(self):
        print "**********************************#4.4.6 获取支付二维码信息**************************************************"
        auth = apimsg.CoreServer_payQRDetail_01
        self.test.test_payQRDetail(auth)
        print "**********************************************************************************************"
    #4.4.7
    def test0031_orderComment(self):
        print "**********************************#4.4.7 订单评价**************************************************"
        auth = apimsg.CoreServer_orderComment_01
        self.test.test_orderComment(auth)
        print "**********************************************************************************************"
    #4.4.8
    def test0032_confirmFinishOrder(self):
        print "**********************************#4.4.8 确认完成**************************************************"
        auth = apimsg.CoreServer_confirmFinishOrder_01
        self.test.test_confirmFinishOrder(auth)
        print "**********************************************************************************************"
    #4.5.1
    def test0033_wechatSubmitPay(self):
        print "**********************************#4.5.1 微信端提交付款**************************************************"
        auth = apimsg.CoreServer_wechatSubmitPay_01
        self.test.test_wechatSubmitPay(auth)
        print "**********************************************************************************************"
    #4.5.2
    def test0034_appSubmitPay(self):
        print "**********************************#4.5.2 移动端提交付款**************************************************"
        auth = apimsg.CoreServer_appSubmitPay_01
        self.test.test_appSubmitPay(auth)
        print "**********************************************************************************************"
    #4.5.3
    def test0035_checkOrderPayStatus(self):
        print "**********************************#4.5.3 订单付款状态**************************************************"
        auth = apimsg.CoreServer_checkOrderPayStatus_01
        self.test.test_checkOrderPayStatus(auth)
        print "**********************************************************************************************"