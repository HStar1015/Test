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
    #2.1.1注册
    def test0001_regist_test(self):
        print "**********************************#2.1.1注册**************************************************"
        auth = apimsg.CoreServer_register_01
        self.test.test_register_test(auth)
        print "**********************************************************************************************"
    #2.1.2登录
    def test0002_login_test(self):
        print "***********************************#2.1.2登录************************************************"
        auth = apimsg.CoreServer_login_01
        self.test.test_login_test(auth)
        print "*********************************************************************************************"
    #2.1.3申请邀请码
    def test0003_applyInvite_test(self):
        print "***********************************#2.1.3申请邀请码******************************************"
        auth = apimsg.CoreServer_applyInvite_01
        self.test.test_applyInvite_test(auth)
        print "*********************************************************************************************"
    #2.1.4修改商家信息
    def test0004_updateInfo_test(self):
        print "****************************************#2.1.4修改商家信息***********************************"
        auth = apimsg.CoreServer_updateInfo_01
        self.test.test_updateInfo_test(auth)
        print "*********************************************************************************************"
    #2.1.5获取商家信息
    def test0005_businessInfo_test(self):
        print "*****************************************#2.1.5获取商家信息***********************************"
        auth = apimsg.CoreServer_businessInfo_01
        self.test.test_businessInfo_test(auth)
        print "**********************************************************************************************"
    #2.1.6更新用户设备id
    def test0006_updateRegistrationId_test(self):
        print "***************************************#2.1.6更新用户设备id***********************************"
        auth = apimsg.CoreServer_updateRegistrationId_01
        self.test.test_updateRegistrationId_test(auth)
        print "**********************************************************************************************"
    #2.2.1新增门店
    def test0007_saveShop_test(self):
        print "***************************************#2.2.1新增门店*****************************************"
        auth =apimsg.CoreServer_saveShop_01
        self.test.test_saveShop_test(auth)
        print "**********************************************************************************************"

    #2.2.2修改门店信息
    def test0008_updateInfo_test(self):
        print "**************************************#2.2.2修改门店信息******************************************"
        auth =apimsg.CoreServer_updateInfo_01
        self.test.test_updateInfo_test(auth)
        print "**********************************************************************************************"

    #2.2.3获取门店列表
    def test0009_shopList_test(self):
        print "**************************************#2.2.3获取门店列表***************************************"
        auth =apimsg.CoreServer_shopList_01
        self.test.test_shopList_test(auth)
        print "***********************************************************************************************"
    #2.2.4获取门店信息
    def test0010_shopInfo_test(self):
        print "**************************************#2.2.4获取门店信息***************************************"
        auth = apimsg.CoreServer_shopList_01
        self.test.test_shopInf_test(auth)
        print "***********************************************************************************************"
    #2.2.5删除门店
    def test0011_deleteShop_test(self):
        print "**************************************#2.2.5删除门店***************************************"
        auth = apimsg.CoreServer_deleteShop_01
        self.test.test_deleteShop_test(auth)
        print "***********************************************************************************************"
    # 2.3.1添加项目
    def test0012_addProject_test(self):
        print "**************************************#2.3.1添加项目***************************************"
        auth = apimsg.CoreServer_addProject_01
        self.test.test_addProject_test(auth)
        print "***********************************************************************************************"
    #2.3.2删除项目
    def test0013_deleteProject_test(self):
        print "**************************************#2.3.2删除项目***************************************"
        auth = apimsg.CoreServer_deleteProject_01
        self.test.test_deleteProject_test(auth)
        print "***********************************************************************************************"
    #2.3.3编辑项目
    def test0014_editProject_test(self):
        print "**************************************#2.3.3编辑项目***************************************"
        auth = apimsg.CoreServer_editProject_01
        self.test.test_editProject_test(auth)
        print "***********************************************************************************************"
    #2.3.4获取项目列表
    def test0015_projectList_test(self):
        print "**************************************#2.3.4获取项目列表***************************************"
        auth = apimsg.CoreServer_projectList_01
        self.test.test_projectList_test(auth)
        print "***********************************************************************************************"
    #2.3.5项目详情
    def test0016_projectDetails_test(self):
        print "**************************************#2.3.5项目详情***************************************"
        auth = apimsg.CoreServer_projectDetails_01
        self.test.test_projectDetails_test(auth)
        print "***********************************************************************************************"
    #2.3.6复制项目
    def test0017_copyProject_test(self):
        print "**************************************#2.3.6复制项目***************************************"
        auth = apimsg.CoreServer_copyProject_01
        self.test.test_copyProject_test(auth)
        print "***********************************************************************************************"
    #2.4.1邀请员工
    def test0018_pushInvitation_test(self):
        print "**************************************#2.4.1邀请员工***************************************"
        auth = apimsg.CoreServer_pushInvitation_01
        self.test.test_pushInvitation_test(auth)
        print "***********************************************************************************************"
    #2.4.2员工列表
    def test0019_personnelList_test(self):
        print "**************************************#2.4.2员工列表***************************************"
        auth = apimsg.CoreServer_personnelList_01
        self.test.test_personnelList_test(auth)
        print "***********************************************************************************************"
    #2.4.3
    def test0020_personnelDetails_test(self):
        print "**************************************#2.4.3员工详情***************************************"
        auth = apimsg.CoreServer_personnelDetails_01
        self.test.test_personnelDetails_test(auth)
        print "***********************************************************************************************"
    #2.4.4
    def test0021_unbind_test(self):
        print "**************************************#2.4.4解除绑定***************************************"
        auth = apimsg.CoreServer_unbind_01
        self.test.test_unbind_test(auth)
        print "***********************************************************************************************"
    #2.4.5
    def test0022_allocationPersonnel_test(self):
        print "**************************************#2.4.5分配员工给门店***************************************"
        auth = apimsg.CoreServer_allocationPersonnel_01
        self.test.test_allocationPersonnel_test(auth)
        print "***********************************************************************************************"
    #2.4.6.1
    def test0023_commentGroupNum_test(self):
        print "**************************************#2.4.6.1员工评论分组数量***************************************"
        auth = apimsg.CoreServer_commentGroupNum_01
        self.test.test_commentGroupNum_test(auth)
        print "***********************************************************************************************"
    #2.4.6.2
    def test0024_commentList_test(self):
        print "**************************************#2.4.6.2员工评论列表***************************************"
        auth = apimsg.CoreServer_commentList_01
        self.test.test_commentList_test(auth)
        print "***********************************************************************************************"
    #2.5.1
    def test0025_customerList_test(self):
        print "**************************************#2.5.1顾客列表***************************************"
        auth = apimsg.CoreServer_customerList_01
        self.test.test_customerList_test(auth)
        print "***********************************************************************************************"
    #2.5.2
    def test0026_customerDetails_test(self):
        print "**************************************#2.5.2顾客详情***************************************"
        auth = apimsg.CoreServer_customerDetails_01
        self.test.test_customerDetails_test(auth)
        print "***********************************************************************************************"
    #2.5.3
    def test0027_allocaCustomer_test(self):
        print "**************************************#2.5.3分配顾客给员工***************************************"
        auth = apimsg.CoreServer_allocationCustomer_01
        self.test.test_allocationCustomer_test(auth)
        print "***********************************************************************************************"
    #2.5.4
    def test0028_expenseRecord_test(self):
        print "**************************************#2.5.4消费记录***************************************"
        auth = apimsg.CoreServer_expenseRecord_01
        self.test.test_expenseRecord_test(auth)
        print "***********************************************************************************************"
    #2.5.5
    def test0029_expenseProject_test(self):
        print "**************************************#2.5.5消费项目***************************************"
        auth = apimsg.CoreServer_expenseProject_01
        self.test.test_expenseProject_test(auth)
        print "***********************************************************************************************"
    #2.5.6
    def test0030_changeRank_test(self):
        print "**************************************#2.5.6改变顾客分组***************************************"
        auth = apimsg.CoreServer_changeRank_01
        self.test.test_changeRank_test(auth)
        print "***********************************************************************************************"
    #2.5.7
    def test0031_rankInfoList_test(self):
        print "**************************************#2.5.7获取分组信息列表***************************************"
        auth = apimsg.CoreServer_rankInfoList_01
        self.test.test_rankInfoList_test(auth)
        print "***********************************************************************************************"
    #2.6.1
    def test0032_findAccountBalace_test(self):
        print "**************************************#2.6.1查询账户余额***************************************"
        auth = apimsg.CoreServer_findAccountBalance_01
        self.test.test_findAccountBalance_test(auth)
        print "***********************************************************************************************"
    #2.6.2
    def test0033_accountRecordList_test(self):
        print "**************************************#2.6.2账户历史记录***************************************"
        auth = apimsg.CoreServer_accountRecordList_01
        self.test.test_accountRecordList_test(auth)
        print "***********************************************************************************************"
    #2.6.3
    def test0034_putApply_test(self):
        print "**************************************#2.6.3提现申请***************************************"
        auth = apimsg.CoreServer_putApply_01
        self.test.test_putApply_test(auth)
        print "***********************************************************************************************"
    #2.6.4
    def test0035_putRecordDetail(self):
        print "**************************************#2.6.4提现记录详情***************************************"
        auth = apimsg.CoreServer_putRecordDetail_01
        self.test.test_putRecordDetail(auth)
        print "***********************************************************************************************"
    #2.6.5
    def test0036_incomeRecordDetail(self):
        print "**************************************#2.6.5进账记录详情***************************************"
        auth = apimsg.CoreServer_incomeRecordDetail_01
        self.test.test_incomeRecordDetail(auth)
        print "***********************************************************************************************"
    #2.7.1
    def test0037_shopCapacity(self):
        print "**************************************#2.7.1店容量***************************************"
        auth = apimsg.CoreServer_shopCapacity_01
        self.test.test_shopCapacity(auth)
        print "***********************************************************************************************"
    #2.7.2
    def test0038_shopDiagnose(self):
        print "**************************************#2.7.2经营诊断***************************************"
        auth = apimsg.CoreServer_shopDiagnose_01
        self.test.test_shopDiagnose(auth)
        print "***********************************************************************************************"
    #2.7.3
    def test0039_getShopCapacity(self):
        print "**************************************#2.7.3获取店容量***************************************"
        auth = apimsg.CoreServer_getShopCapacity_01
        self.test.test_getShopCapacity(auth)
        print "***********************************************************************************************"
    #2.7.4
    def test0040_getShopDiagnose(self):
        print "**************************************#2.7.4获取店经营诊断***************************************"
        auth = apimsg.CoreServer_getShopDiagnose_01
        self.test.test_getShopDiagnose(auth)
        print "***********************************************************************************************"
    #2.8.1
    def test0041_createActivity(self):
        print "**************************************#2.8.1新建活动***************************************"
        auth = apimsg.CoreServer_createActivity_01
        self.test.test_createActivity(auth)
        print "***********************************************************************************************"
    #2.8.2
    def test0042_activityList(self):
        print "**************************************#2.8.2活动列表***************************************"
        auth = apimsg.CoreServer_activityList_01
        self.test.test_activityList(auth)
        print "***********************************************************************************************"
    #2.8.3
    def test0043_activityDetail(self):
        print "**************************************#2.8.3活动详情***************************************"
        auth = apimsg.CoreServer_activityDetail_01
        self.test.test_activityDetail(auth)
        print "***********************************************************************************************"
    #2.8.4
    def test0044_activityQr(self):
        print "**************************************#2.8.4活动二维码及分享**************************************"
        auth = apimsg.CoreServer_activityQr_01
        self.test.test_activityQr(auth)
        print "***********************************************************************************************"
    #2.8.5
    def test0045_activityPersonnelList(self):
        print "**************************************#2.8.5美容拓客列表**************************************"
        auth = apimsg.CoreServer_activityPersonnelList_01
        self.test.test_activityPersonnelList(auth)
        print "***********************************************************************************************"
    #2.8.6
    def test0046_activityChooseProjectList(self):
        print "**************************************#2.8.6 活动选择项目列表**************************************"
        auth = apimsg.CoreServer_activityChooseProjectList_01
        self.test.test_activityChooseProjectList(auth)
        print "***********************************************************************************************"
###############################################2017-04-12-新增接口--2.2.6店数据统计#########################################
    #2.2.6.1
    def test0047_shopStatics(self):
        print "**************************************#2.2.6.1店业绩消耗统计**************************************"
        auth = apimsg.CoreServer_shopStatics_01
        self.test.test_shopStatics_test(auth)
        print "***********************************************************************************************"
    # 2.2.6.2
    def test0048_saleStatics(self):
        print "**************************************#2.2.6.2进店顾客统计**************************************"
        auth = apimsg.CoreServer_saleStatistics_01
        self.test.test_saleStatics_test(auth)
        print "***********************************************************************************************"
    # 2.2.6.3
    def test0049_newCustomerStatistics(self):
        print "**************************************#2.2.6.3新店量统计**************************************"
        auth = apimsg.CoreServer_newCustomerStatistics_01
        self.test.test_newCustomerStatistics_test(auth)
        print "***********************************************************************************************"
    # 2.2.6.4
    def test0050_projectSaleStatistics(self):
        print "**************************************#2.2.6.4项目销售统计**************************************"
        auth = apimsg.CoreServer_projectSaleStatistics_01
        self.test.test_projectSaleStatistics_test(auth)
        print "***********************************************************************************************"
###############################################2017-04-10-新增接口--2.4.7员工日志########################################
    #2.4.7.1
    def test0051_daySummarizeList(self):
        print "**************************************#2.4.7.1员工日总结列表**************************************"
        auth = apimsg.CoreServer_daySummarizeList_01
        self.test.test_daySummarizeList(auth)
        print "***********************************************************************************************"
    # 2.4.7.2
    def test0051_daySummarizeDetail(self):
        print "**************************************#2.4.7.2员工日总结详情**************************************"
        auth = apimsg.CoreServer_daySummarizeDetail_01
        self.test.test_daySummarizeDetail(auth)
        print "***********************************************************************************************"
    #2.4.7.3
    def test0052_monthPlanList(self):
        print "**************************************#2.4.7.3 员工月计划列表**************************************"
        auth = apimsg.CoreServer_monthPlanList_01
        self.test.test_monthPlanList(auth)
        print "***********************************************************************************************"
    # 2.4.7.4
    def test0053_monthDetail(self):
        print "**************************************#2.4.7.4 员工月计划详情**************************************"
        auth = apimsg.CoreServer_monthDetail_01
        self.test.test_monthPlanDetail(auth)
        print "***********************************************************************************************"

    ###############################################2017-04-11-新增接口--2.4.8员工数据########################################
    #2.4.8.1
    def test0054_operationCaseList(self):
        print "**************************************#2.4.8.1	员工操作业绩情况列表**************************************"
        auth = apimsg.CoreServer_operationCaseList_01
        self.test.test_operationCaseList(auth)
        print "***********************************************************************************************"
    # 2.4.8.2
    def test0055_operationCaseDetail(self):
        print "**************************************#2.4.8.2	销售项目详情**************************************"
        auth = apimsg.CoreServer_operationDetail_01
        self.test.test_operationCaseDetail(auth)
        print "***********************************************************************************************"
    ###############################################2017-04-07-新增接口--2.5.8顾客卡项########################################
    #2.5.8.1
    def test0056_customerCardList(self):
        print "**************************************#2.5.8.1 顾客卡项列表**************************************"
        auth = apimsg.CoreServer_customerCardList_01
        self.test.test_customerCardList(auth)
        print "***********************************************************************************************"
    # 2.5.8.2
    def test0057_cardConsummerDetailList(self):
        print "**************************************#2.5.8.2卡项消费明细列表**************************************"
        auth = apimsg.CoreServer_cardConsummerDetailList_01
        self.test.test_cardConsummerDetailList(auth)
        print "***********************************************************************************************"