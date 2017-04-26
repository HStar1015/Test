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
        print "**********************************#!!!3.1.6设置工作时间**************************************************"
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
    #3.4.7
    def test0028_rankInfoList(self):
        print "**********************************#3.4.7获取分组信息列表**************************************************"
        auth = apimsg.CoreServer_rankInfoList_01
        self.test.test_rankInfoList(auth)
        print "**********************************************************************************************"
    #3.5.1
    def test0029_commentGroupNum(self):
        print "**********************************#3.5.1我的评论分组数量**************************************************"
        auth = apimsg.CoreServer_commentGroupNum_01
        self.test.test_commentGroupNum(auth)
        print "**********************************************************************************************"
    #3.5.2
    def test0030_commentList(self):
        print "**********************************#3.5.2我的评论列表**************************************************"
        auth = apimsg.CoreServer_commentList_01
        self.test.test_commentList(auth)
        print "**************** ******************************************************************************"
    #3.6.1
    def test0031_activityList(self):
        print "**********************************#3.6.1活动列表**************************************************"
        auth = apimsg.CoreServer_activityList_01
        self.test.test_activityList(auth)
        print "**************** ******************************************************************************"
    #3.6.2
    def test0032_activityDetail(self):
        print "**********************************#3.6.2活动详情**************************************************"
        auth = apimsg.CoreServer_activityDetail_01
        self.test.test_activityDetail(auth)
        print "**************** ******************************************************************************"
    #3.6.3
    def test0033_activityQr(self):
        print "**********************************#3.6.3 活动二维码及分享**************************************************"
        auth = apimsg.CoreServer_activityQr_01
        self.test.test_activityQr(auth)
        print "**************** ******************************************************************************"

        # ******************************2017-03-29-新增接口-----员工计划总结相关*****************************************
    #3.7.1
    def test0034_createPlan(self):
        print "**********************************#3.7.1新增月计划**************************************************"
        auth = apimsg.CoreServer_createPlan_01
        self.test.test_createPlan(auth)
        print "**************** ******************************************************************************"
    #3.7.2
    def test0035_editPlan(self):
        print "**********************************#3.7.2编辑月计划**************************************************"
        auth = apimsg.CoreServer_editPlan_01
        self.test.test_editPlan(auth)
        print "**************** ******************************************************************************"
    #3.7.3
    def test0036_selectPlanDetail(self):
        print "**********************************#3.7.3查询月计划详情**************************************************"
        auth = apimsg.CoreServer_selectPlanDetail_01
        self.test.test_selectPlanDetail(auth)
        print "**************** ******************************************************************************"
    #3.7.4
    def test0037_selectCustomerList(self):
        print "**********************************#3.7.4 查询顾客列表**************************************************"
        auth = apimsg.CoreServer_selectCustomerList_01
        self.test.test_selectCustomerList(auth)
        print "**************** ******************************************************************************"
    #3.7.5
    def test0038_selectPlanList(self):
        print "**********************************#3.7.5查询月计划列表**************************************************"
        auth = apimsg.CoreServer_selectPlanList_01
        self.test.test_selectPlanList(auth)
        print "**************** ******************************************************************************"
    #3.7.6
    def test0039_createDaySummarize(self):
        print "**********************************#3.7.6新增日总结**************************************************"
        auth = apimsg.CoreServer_createDaySummarize_01
        self.test.test_createDaySummarize(auth)
        print "**************** ******************************************************************************"
    #3.7.7
    def test0040_editDaySummarize(self):
        print "**********************************#3.7.7编辑日总结**************************************************"
        auth = apimsg.CoreServer_editDaySummarize_01
        self.test.test_editDaySummarize(auth)
        print "**************** ******************************************************************************"
    #3.7.8
    def test0041_selectDaySummarize(self):
        print "**********************************#3.7.8查询日总结详情**************************************************"
        auth = apimsg.CoreServer_selectDaySummarizeDetail_01
        self.test.test_selectDaySummarizeDetail(auth)
        print "**************** ******************************************************************************"
    # 3.7.9
    def test0042_selectSummarizeList(self):
        print "**********************************#3.7.8查询日总结列表*************************************************"
        auth = apimsg.CoreServer_selectSummarizeList_01
        self.test.test_selectSummarizeList(auth)
        print "**************** ******************************************************************************"
    #******************************2017-03-30-新增接口-----顾客卡项相关*****************************************
    # 3.4.8.1
    def test0043_createCard(self):
        print "**********************************#3.4.8.1新增卡项**************************************************"
        auth = apimsg.CoreServer_createCard_01
        self.test.test_createCard(auth)
        print "**********************************************************************************************"
    # #3.4.8.2
    def test0043_createCard(self):
        print "**********************************#3.4.8.2编辑卡项**************************************************"
        auth = apimsg.CoreServer_editCard_01
        self.test.test_editCard(auth)
        print "**********************************************************************************************"
    # #3.4.8.3
    def test0044_cardDetail(self):
        print "**********************************#3.4.8.3卡项详情**************************************************"
        auth = apimsg.CoreServer_cardDetail_01
        self.test.test_cardDetail(auth)
        print "**********************************************************************************************"
    # #3.4.8.4
    def test0045_customerCardList(self):
        print "**********************************#3.4.8.4顾客卡项列表**************************************************"
        auth = apimsg.CoreServer_customerCardList_01
        self.test.test_customerCardList(auth)
        print "**********************************************************************************************"
    # #3.4.8.5
    def test0046_operationCard(self):
        print "**********************************#3.4.8.5操作卡项**************************************************"
        auth = apimsg.CoreServer_operationCard_01
        self.test.test_operationCard(auth)
        print "**********************************************************************************************"
    # #3.4.8.6
    def test0047_cardConsummerDetailList(self):
        print "**********************************#3.4.8.6卡项消费明细列表**************************************************"
        auth = apimsg.CoreServer_cardConsummerDetailList_01
        self.test.test_cardConsummerDetailList(auth)
        print "**********************************************************************************************"