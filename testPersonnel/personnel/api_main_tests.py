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
    #3.2.2
    def test0011_chooseProject(self):
        print "**********************************#3.2.2选择项目**************************************************"
        auth = apimsg.CoreServer_chooseProject_01
        self.test.test_chooseProject(auth)
        print "**********************************************************************************************"
    #3.2.3
    def test0012_myProjectList(self):
        print "**********************************#3.2.3我的项目列表**************************************************"
        auth = apimsg.CoreServer_myProjectList_01
        self.test.test_myProjectList(auth)
        print "**********************************************************************************************"
    #3.2.4
    def test013_delProject(self):
        print "**********************************#3.2.4删除我的项目**************************************************"
        auth = apimsg.CoreServer_delProject_01
        self.test.test_delProject(auth)
        print "**********************************************************************************************"
    #3.2.5
    def test014_projectDetails(self):
        print "**********************************#3.2.5项目详情**************************************************"
        auth = apimsg.CoreServer_projectDetails_01
        self.test.test_projectDetailsa(auth)
        print "**********************************************************************************************"
    #3.3.1
    def test015_projectDetails(self):
        print "**********************************#3.3.1我的订单分组数量**************************************************"
        auth = apimsg.CoreServer_orderGroupNum_01
        self.test.test_orderGroupNum(auth)
        print "**********************************************************************************************"
    #3.3.2
    def test016_myOrderList(self):
        print "**********************************#3.3.2我的订单列表**************************************************"
        auth = apimsg.CoreServer_myOrderList_01
        self.test.test_myOrderList(auth)
        print "**********************************************************************************************"
    #3.3.3
    def test017_orderDetail(self):
        print "**********************************#3.3.3订单详情**************************************************"
        auth = apimsg.CoreServer_orderDetail_01
        self.test.test_orderDetail(auth)
        print "**********************************************************************************************"
    #3.3.4
    def test0018_cancelOrder(self):
        print "**********************************#3.3.4取消预约**************************************************"
        auth = apimsg.CoreServer_cancelOrder_01
        self.test.test_cancelOrder(auth)
        print "**********************************************************************************************"
    #3.3.5
    def test0019_confirmFinishOrder(self):
        print "**********************************#3.3.5确认完成**************************************************"
        auth = apimsg.CoreServer_confirmFinishOrder_01
        self.test.test_confirmFinishOrder(auth)
        print "**********************************************************************************************"
    #3.3.6
    def test0020_scanFinishOrder(self):
        print "**********************************#3.3.6扫码确认完成**************************************************"
        auth = apimsg.CoreServer_scanFinishOrder_01
        self.test.test_scanFinishOrder(auth)
        print "**********************************************************************************************"
    #3.3.7
    def test0021_orderSave(self):
        print "**********************************#3.3.7美容师手动添加订单**************************************************"
        auth = apimsg.CoreServer_orderSave_01
        self.test.test_orderSave(auth)
        print "**********************************************************************************************"
    #3.4.1
    def test0022_customerList(self):
        print "**********************************#3.4.1我的顾客列表**************************************************"
        auth = apimsg.CoreServer_customerList_01
        self.test.test_customerList(auth)
        print "**********************************************************************************************"
    #3.4.2
    def test0023_changeRemark(self):
        print "**********************************#3.4.2改变顾客备注**************************************************"
        auth = apimsg.CoreServer_changeRemark_01
        self.test.test_changeRemark(auth)
        print "**********************************************************************************************"
    #3.4.3
    def test0024_changeRank(self):
        print "**********************************#3.4.3改变顾客分组**************************************************"
        auth = apimsg.CoreServer_changeRank_01
        self.test.test_changeRank(auth)
        print "**********************************************************************************************"
    #3.4.4
    def test0025_customerDetails(self):
        print "**********************************#3.4.4顾客详情**************************************************"
        auth = apimsg.CoreServer_customerDetails_01
        self.test.test_customerDetails(auth)
        print "**********************************************************************************************"
    #3.4.5
    def test0026_expenseRecord(self):
        print "**********************************#3.4.5消费记录**************************************************"
        auth = apimsg.CoreServer_expenseRecord_01
        self.test.test_expenseRecord(auth)
        print "**********************************************************************************************"
    #3.4.6
    def test0027_expenseProject(self):
        print "**********************************#3.4.6消费项目**************************************************"
        auth = apimsg.CoreServer_expenseProject_01
        self.test.test_expenseProject(auth)
        print "**********************************************************************************************"