# -*- coding: utf-8 -*-
import actions
class test_core_server():
    # ************************3.1*******************************
    # 3.1.1
    def test_register_test(self, register_obj):
        res = actions.register(register_obj.url,register_obj.phone,register_obj.password,register_obj.authCode,
                                    register_obj.X_Type)

    #3.1.2
    def test_login_test(self,login_obj):
        res = actions.login(login_obj.url,login_obj.phone,login_obj.password,login_obj.X_Type)
    #3.1.3
    def test_acceptInvitation_test(self,acceptInvitation_obj):
        res = actions.acceptInvitation(acceptInvitation_obj.url,acceptInvitation_obj.id,acceptInvitation_obj.businessId,
                                       acceptInvitation_obj.X_Type)
    #3.1.4
    def test_personnelInfo_test(self,personnelInfo_obj):
        res = actions.personnelInfo(personnelInfo_obj.url,personnelInfo_obj.id,personnelInfo_obj.X_Type)
    #3.1.5
    def test_updateInfo(self,updateInfo_obj):
        res = actions.updateInfo(updateInfo_obj.url,updateInfo_obj.id,updateInfo_obj.name,updateInfo_obj.sex,updateInfo_obj.X_Type,updateInfo_obj.files)
    #3.1.6
    def test_workTime(self,workTime_obj):
        res = actions.workTime(workTime_obj.url,workTime_obj.id,workTime_obj.monStart,workTime_obj.monEnd,workTime_obj.tueStart,
                               workTime_obj.tueEnd,workTime_obj.wedStart,workTime_obj.wedEnd,workTime_obj.thuStart,workTime_obj.thuEnd,
                               workTime_obj.friStart,workTime_obj.friEnd,workTime_obj.satStart,workTime_obj.satEnd,workTime_obj.sunStart,
                               workTime_obj.sunEnd,workTime_obj.ifMonWork,workTime_obj.ifTueWork,workTime_obj.ifWedWork,
                               workTime_obj.ifThuWork,workTime_obj.ifFriWork,workTime_obj.ifSatWork,workTime_obj.ifSunWork)
    #3.1.7
    def test_getWorkTime(selfm,getWorkTime_obj):
        res = actions.getWorkTime(getWorkTime_obj.url ,getWorkTime_obj.personnelId ,getWorkTime_obj.X_Type)
    #3.1.8
    def test_shopInfo(self,shopInfo_obj):
        res = actions.shopInfo(shopInfo_obj.url,shopInfo_obj.shopId,shopInfo_obj.X_Type)
    #3.1.9
    def test_updateRegistration(self,updateRegistration_obj):
        res = actions.updateRegistrationId(updateRegistration_obj.url,updateRegistration_obj.id,updateRegistration_obj.registrationId,
                                           updateRegistration_obj.X_Type)
    #*********************************************3.2********************************************
    #3.2.1
    def test_projectList(self,projectList_obj):
        res = actions.projecList(projectList_obj.url,projectList_obj.shopId,projectList_obj.personnelId,projectList_obj.pageSize,
                                 projectList_obj.X_Type)
    #3.2.2
    def test_chooseProject(self,chooseProject_obj):
        res = actions.chooseProject(chooseProject_obj.url,chooseProject_obj.projectIds,chooseProject_obj.personnelId,
                                    chooseProject_obj.X_Type)
    #3.2.3
    def test_myProjectList(self,myProjectList_obj):
        res = actions.myProjectList(myProjectList_obj.url,myProjectList_obj.shopId,myProjectList_obj.personnelId,
                                    myProjectList_obj.pageSize,myProjectList_obj.X_Type)
    #3.2.4
    def test_delProject(self,delProject_obj):
        res = actions.delProject(delProject_obj.url,delProject_obj.projectIds,delProject_obj.personnelId,delProject_obj.X_Type)
    #3.2.5
    def test_projectDetailsa(self,projectDetails_obj):
        res = actions.projectDetails(projectDetails_obj.url,projectDetails_obj.id,projectDetails_obj.X_Type)
    #*******************************************3.3*****************************************
    #3.3.1
    def test_orderGroupNum(self,orderGroupNum_obj):
        res = actions.orderGroupNum(orderGroupNum_obj.url ,orderGroupNum_obj.shopId,
                                    orderGroupNum_obj.personnelId,orderGroupNum_obj.X_Type)
    #3.3.2
    def test_myOrderList(self, myOrderList_obj):
        res = actions.myOrderList(myOrderList_obj.url, myOrderList_obj.shopId,
                                    myOrderList_obj.personnelId,myOrderList_obj.pageSize, myOrderList_obj.X_Type)
    #3.3.3
    def test_orderDetail(self,orderDetail_obj):
        res= actions.orderDetail(orderDetail_obj.url,orderDetail_obj.personnelId,orderDetail_obj.orderNo,orderDetail_obj.X_Type)
    #3.3.4
    def test_cancelOrder(self,cancelOrder_obj):
        res = actions.cancelOrder(cancelOrder_obj.url,cancelOrder_obj.personnelId,cancelOrder_obj.orderNo,cancelOrder_obj.X_Type)
    #3.3.5
    def test_confirmFinishOrder(self,confirmFinishOrder_obj):
        res = actions.confirmFinishOrder(confirmFinishOrder_obj.url,confirmFinishOrder_obj.personnelId,confirmFinishOrder_obj.orderNo,confirmFinishOrder_obj.X_Type)
    #3.3.6
    def test_scanFinishOrder(self,scanFinishOrder_obj):
        res = actions.scanFinishOrder(scanFinishOrder_obj.url,scanFinishOrder_obj.personnelId,scanFinishOrder_obj.payCode,
                                      scanFinishOrder_obj.X_Type)
    #3.3.7
    def test_orderSave(self,orderSave_obj):
        res = actions.orderSave(orderSave_obj.url,orderSave_obj.projectId,orderSave_obj.personnelId,orderSave_obj.makeStartDate,
                                orderSave_obj.makeEndDate,orderSave_obj.priceType,orderSave_obj.reserveName,orderSave_obj.reservePhone,orderSave_obj.X_Type)
    #****************************************3.4**********************************************************
    #3.4.1
    def test_customerList(self,customerList_obj):
        res = actions.customerList(customerList_obj.url,customerList_obj.shopId,customerList_obj.personnelId,
                                   customerList_obj.pageSize,customerList_obj.X_Type)
    #3.4.2
    def test_changeRemark(self,changeRemark_obj):
        res = actions.changeRemark(changeRemark_obj.url,changeRemark_obj.shopId,changeRemark_obj.personnelId,
                                   changeRemark_obj.remark,changeRemark_obj.customerId,changeRemark_obj.X_Type)
    #3.4.3
    def test_changeRank(self,changeRank_obj):
        res = actions.changeRank(changeRank_obj.url,changeRank_obj.shopId,changeRank_obj.rankId,changeRank_obj.customerIds,
                                 changeRank_obj.X_Type)
    #3.4.4
    def test_customerDetails(self,customerDetails_obj):
        res = actions.customerDetails(customerDetails_obj.url,customerDetails_obj.shopId,customerDetails_obj.customerId,
                                      customerDetails_obj.X_Type)
    #3.4.5
    def test_expenseRecord(self,expenseRecord_obj):
        res = actions.expenseRecord(expenseRecord_obj.url,expenseRecord_obj.customerId,expenseRecord_obj.shopId,expenseRecord_obj.pageSize,
                                    expenseRecord_obj.X_Type)
    #3.4.6
    def test_expenseProject(self,expenseProject_obj):
        res = actions.expenseProject(expenseProject_obj.url,expenseProject_obj.customerId,expenseProject_obj.shopId,expenseProject_obj.pageSize,
                                     expenseProject_obj.X_Type)
    #3.4.7
    def test_rankInfoList(self,rankInfoList_obj):
        res = actions.rankInfoList(rankInfoList_obj.url,rankInfoList_obj.shopId,rankInfoList_obj.personnelId,rankInfoList_obj.X_Type)
    ############新增接口###########
    #3.4.8.1
    def test_createCard(self,createCard_obj):
        res = actions.createCard(createCard_obj.url,createCard_obj.shopId,createCard_obj.personnelId,createCard_obj.customerId,createCard_obj.cardType,
                                 createCard_obj.name,createCard_obj.remark,createCard_obj.validityDate,createCard_obj.X_Type)
    # 3.4.8.2
    # 3.4.8.3
    # 3.4.8.4
    # 3.4.8.5
    # 3.4.8.6
    #******************************************3.5********************************************
    #3.5.1
    def test_commentGroupNum(self,commentGroupNum_obj):
        res = actions.commentGroupNum(commentGroupNum_obj.url,commentGroupNum_obj.personnelId)
    #3.5.2
    def test_commentList(self,commentList_obj):
        res = actions.commentList(commentList_obj.url,commentList_obj.personnelId,commentList_obj.commentLevel,commentList_obj.pageSize ,commentList_obj.X_Type)
    # ******************************************3.6*********************************************
    #3.6.1
    def test_activityList(self,activityList_obj):
        res = actions.activityList(activityList_obj.url,activityList_obj.shopId,activityList_obj.pageSize,activityList_obj.X_Type)
    #3.6.2
    def test_activityDetail(self,activityDetail_obj):
        res = actions.activityDetail(activityDetail_obj.url,activityDetail_obj.activityId,activityDetail_obj.shopId,
                                     activityDetail_obj.pageSize,activityDetail_obj.X_Type)
    #3.6.3
    def test_activityQr(self,activityQr_obj):
        res = actions.activityQr(activityQr_obj.url,activityQr_obj.shopId,activityQr_obj.activityId,
                                 activityQr_obj.personnelId,activityQr_obj.X_Type)
    # ******************************************3.7*********************************************
    #3.7.1
    def test_createPlan(self,createPlan_obj):
        res = actions.createPlan(createPlan_obj.url,createPlan_obj.month,createPlan_obj.personnelId,createPlan_obj.personnelPlanDetailDtos,
                                 createPlan_obj.customerRankId,createPlan_obj.planPerformance,createPlan_obj.planIntroduce,
                                 createPlan_obj.X_Type)
    #3.7.2
    def test_editPlan(self, editPlan_obj):
        res = actions.editPlan(editPlan_obj.url, editPlan_obj.id,
                               editPlan_obj.personnelPlanDetailDtos,
                               editPlan_obj.customerRankId, editPlan_obj.planPerformance,
                               editPlan_obj.planIntroduce,
                               editPlan_obj.X_Type)
    #3.7.3
    def test_selectPlanDetail(self,selectPlanDetail_obj):
        res = actions.selectPlanDetail(selectPlanDetail_obj.url,selectPlanDetail_obj.planId,selectPlanDetail_obj.X_Type)
    #3.7.4
    def test_selectCustomerList(self,selectCustomerList_obj):
        res = actions.selectCustomerList(selectCustomerList_obj.url,selectCustomerList_obj.shopId,selectCustomerList_obj.personnelId,
                                         selectCustomerList_obj.operationType,selectCustomerList_obj.recordType,selectCustomerList_obj.customerType,
                                         selectCustomerList_obj.X_Type)
    #3.7.5
    def test_selectPlanList(self,selectPlanList_obj):
        res = actions.selectPlanList(selectPlanList_obj.url,selectPlanList_obj.personnelId,selectPlanList_obj.X_Type)
    #3.7.6
    def test_createDaySummarize(self,createDaySummarize_obj):
        res = actions.createDaySummarize(createDaySummarize_obj.url,createDaySummarize_obj.personnelId,createDaySummarize_obj.day,
                                         createDaySummarize_obj.dayPerformance,createDaySummarize_obj.dayExpend,createDaySummarize_obj.dayOrder,
                                         createDaySummarize_obj.newExperienceIntroduce,createDaySummarize_obj.newExperienceDevelop,
                                         createDaySummarize_obj.newTransactionIntroduce,createDaySummarize_obj.newTransactionDevelop,
                                         createDaySummarize_obj.summary,createDaySummarize_obj.performanceList,createDaySummarize_obj.customerRankId,
                                         createDaySummarize_obj.planPerformance,createDaySummarize_obj.customerType,createDaySummarize_obj.expendList,
                                         createDaySummarize_obj.X_Type)
    #3.7.7
    def test_editDaySummarize(self, editDaySummarize_obj):
        res = actions.editDaySummarize(editDaySummarize_obj.url, editDaySummarize_obj.planId,editDaySummarize_obj.id,
        editDaySummarize_obj.day,editDaySummarize_obj.dayPerformance, editDaySummarize_obj.dayExpend,
        editDaySummarize_obj.dayOrder,editDaySummarize_obj.newExperienceIntroduce,
        editDaySummarize_obj.newExperienceDevelop, editDaySummarize_obj.newTransactionIntroduce,
        editDaySummarize_obj.newTransactionDevelop,editDaySummarize_obj.summary, editDaySummarize_obj.performanceList,
        editDaySummarize_obj.customerRankId,editDaySummarize_obj.planPerformance, editDaySummarize_obj.customerType,
        editDaySummarize_obj.expendList,editDaySummarize_obj.X_Type)
    #3.7.8
    def test_selectDaySummarizeDetail(self,selectDaySummarizeDetail_obj):
        res = actions.selectDaySummarizeDetail(selectDaySummarizeDetail_obj.url,selectDaySummarizeDetail_obj.summarizeId,selectDaySummarizeDetail_obj.X_Type)
    #3.7.9
    def test_selectSummarizeList(self,selectSummarizeList_obj):
        res = actions.selectSummarizeList(selectSummarizeList_obj.url,selectSummarizeList_obj.planId,selectSummarizeList_obj.X_Type)


