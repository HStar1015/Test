# -*- coding: utf-8 -*-
import actions
class test_core_server():
    # ************************2.1*******************************
    # 2.1.1
    def test_register_test(self, register_obj):
        res = actions.register_test(register_obj.url,register_obj.phone,register_obj.password,register_obj.authCode,
                                    register_obj.inviteCode,register_obj.X_Type)
    #2.1.2
    def test_login_test(self,login_test_obj):
        res = actions.login_test(login_test_obj.url,login_test_obj.phone,login_test_obj.password,
                                 login_test_obj.X_Type)
    #2.1.3
    def test_applyInvite_test(self,applyInvite_test_obj):
        res = actions.applyInvite_test(applyInvite_test_obj.url,applyInvite_test_obj.phone,applyInvite_test_obj.name,
                                       applyInvite_test_obj.provinceId,applyInvite_test_obj.cityId,applyInvite_test_obj.areaId,
                                       applyInvite_test_obj.X_Type)
    #2.1.4
    def test_updateInfo_test(self,updateInfo_test_obj):

        res = actions.updateInfo_test(updateInfo_test_obj.url, updateInfo_test_obj.id, updateInfo_test_obj.X_Type)
    #2.1.5
    def test_businessInfo_test(self, businessInfo_test_obj):

        res = actions.businessInfo_test(businessInfo_test_obj.url, businessInfo_test_obj.id, businessInfo_test_obj.X_Type)
    #2.1.6
    def test_updateRegistrationId_test(self,updateRegistrationId_obj):
        res = actions.updateRegistrationId(updateRegistrationId_obj.url,updateRegistrationId_obj.id,
                                           updateRegistrationId_obj.registrationId,updateRegistrationId_obj.X_Type)

    # ************************2.2*******************************
    #2.2.1
    def test_saveShop_test(self,saveShop_obj):
        res = actions.saveShop(saveShop_obj.url,saveShop_obj.businessId,saveShop_obj.phone,saveShop_obj.shopName,saveShop_obj.shortName,
                               saveShop_obj.description,saveShop_obj.provinceId,saveShop_obj.cityId,saveShop_obj.areaId,saveShop_obj.address,
                               saveShop_obj.X_Type,saveShop_obj.files)

    def test_updateInfo_test(self, updateInfo_obj):
        res = actions.saveShop(updateInfo_obj.url, updateInfo_obj.businessId, updateInfo_obj.phone, updateInfo_obj.shopName,
                               updateInfo_obj.shortName,
                               updateInfo_obj.description, updateInfo_obj.provinceId, updateInfo_obj.cityId,
                               updateInfo_obj.areaId, updateInfo_obj.address,
                               updateInfo_obj.X_Type, updateInfo_obj.files)
    #2.2.3
    def test_shopList_test(self,shopList_obj):
        res = actions.shopList(shopList_obj.url,shopList_obj.businessId,shopList_obj.X_Type)
    #2.2.4
    def test_shopInf_test(self,shopInfo_obj):
        res = actions.shopInfo(shopInfo_obj.url,shopInfo_obj.id,shopInfo_obj.X_Type)
    #2.2.5
    def test_deleteShop_test(self,deleteShop_obj):
        res = actions.deleteShop(deleteShop_obj.url,deleteShop_obj.id,deleteShop_obj.businessId,deleteShop_obj.X_Type)
    #2.2.6.1
    def test_shopStatics_test(self,shopStatics_obj):
        res = actions.shopStatics(shopStatics_obj.url,shopStatics_obj.shopId,shopStatics_obj.X_Type)
    # 2.2.6.2
    def test_saleStatics_test(self, saleStatics_obj):
        res = actions.saleStatics(saleStatics_obj.url, saleStatics_obj.shopId, saleStatics_obj.X_Type)
    # 2.2.6.3
    def test_newCustomerStatistics_test(self, newCustomerStatistics_obj):
        res = actions.newCustomerStatistics(newCustomerStatistics_obj.url, newCustomerStatistics_obj.shopId, newCustomerStatistics_obj.X_Type)
    # 2.2.6.4
    def test_projectSaleStatistics_test(self, projectSaleStatistics_obj):
        res = actions.projectSaleStatistics(projectSaleStatistics_obj.url, projectSaleStatistics_obj.shopId, projectSaleStatistics_obj.X_Type)
    # ************************2.3*************************************************************************************************
    #2.3.1
    def test_addProject_test(self,addProject_obj):
        res = actions.addProject(addProject_obj.url,addProject_obj.businessId,addProject_obj.shopIds,addProject_obj.projectName,
                                 addProject_obj.groupNo,addProject_obj.unitPrice,addProject_obj.coursePrice,addProject_obj.courseRemark,
                                 addProject_obj.description,addProject_obj.duration,addProject_obj.applyPerson,addProject_obj.brand,
                                 addProject_obj.noticeMatters,addProject_obj.X_Type,addProject_obj.files)
    #2.3.2
    def test_deleteProject_test(self,deleteProject_obj):
        res = actions.deleteProject(deleteProject_obj.url,deleteProject_obj.id,deleteProject_obj.X_Type)
    #2.3.3
    def test_editProject_test(self,editProject_obj):
        res = actions.editProject(editProject_obj.url,editProject_obj.id,editProject_obj.projectName,
                                 editProject_obj.groupNo,editProject_obj.unitPrice,editProject_obj.coursePrice,editProject_obj.courseRemark,
                                 editProject_obj.description,editProject_obj.duration,editProject_obj.applyPerson,editProject_obj.brand,
                                 editProject_obj.noticeMatters,editProject_obj.X_Type,editProject_obj.files,editProject_obj.fileUuid)
    #2.3.4
    def test_projectList_test(self,projectList_obj):
        res = actions.projectList(projectList_obj.url,projectList_obj.shopId,projectList_obj.pageSize,projectList_obj.X_Type)
    #2.3.5
    def test_projectDetails_test(self,projectDetails_obj):
        res = actions.projectDetails(projectDetails_obj.url ,projectDetails_obj.id,projectDetails_obj.X_Type)
    #2.3.6
    def test_copyProject_test(self,copyProject_obj):
        res = actions.copyProject(copyProject_obj.url,copyProject_obj.businessId,copyProject_obj.shopId,copyProject_obj.projectIds,copyProject_obj.X_Type)
    # ***************************************2.4.1************************************
    #2.4.1
    def test_pushInvitation_test(self,pushInvitation_obj):
        res = actions.pushIncvitation(pushInvitation_obj.url,pushInvitation_obj.personnelPhone,pushInvitation_obj.businessId,
                                      pushInvitation_obj.shopId,pushInvitation_obj.phone,pushInvitation_obj.X_Type)
    #2.4.2
    def test_personnelList_test(self,personnelList_obj):
        res = actions.personnelList(personnelList_obj.url,personnelList_obj.businessId,personnelList_obj.pageSize,
                                    personnelList_obj.X_Type)
    #2.4.3
    def test_personnelDetails_test(self,personnelDetails_obj):
        res = actions.personnelDetails(personnelDetails_obj.url,personnelDetails_obj.id,
                                    personnelDetails_obj.X_Type)
    #2.4.4
    def test_unbind_test(self,unbind_obj):
        res = actions.unbind(unbind_obj.url,unbind_obj.id,unbind_obj.businessId,unbind_obj.X_Type)
    #2.4.5
    def test_allocationPersonnel_test(self,allocationPersonnel_obj):
        res = actions.allocationPersonnel(allocationPersonnel_obj.url,allocationPersonnel_obj.businessId, allocationPersonnel_obj.shopId,
                                          allocationPersonnel_obj.personnelIds,allocationPersonnel_obj.X_Type,)
    #2.4.6.1
    def test_commentGroupNum_test(self,commentGroupNum_obj):
        res = actions.commentGroupNum(commentGroupNum_obj.url,commentGroupNum_obj.personnelId,commentGroupNum_obj.X_Type)
    #2.4.6.2
    def test_commentList_test(self,commentList_obj):
        res = actions.commentList(commentList_obj.url,commentList_obj.personnelId,
                                      commentList_obj.commentLevel,commentList_obj.pageSize,commentList_obj.X_Type)
    #2.4.7.1
    def test_daySummarizeList(self,daySummarizeList_obj):
        res = actions.daySummarizeList(daySummarizeList_obj.url,daySummarizeList_obj.day,daySummarizeList_obj.shopId,daySummarizeList_obj.pageSize,
                                       daySummarizeList_obj.X_Type)
    #2.4.7.2
    def test_daySummarizeDetail(self,daySummarizeDetail_obj):
        res = actions.daySummarizeDetail(daySummarizeDetail_obj.url,daySummarizeDetail_obj.summarizeId,daySummarizeDetail_obj.X_Type)
    #2.4.7.3
    def test_monthPlanList(self,monthPlanList_obj):
        res = actions.monthPlanList(monthPlanList_obj.url,monthPlanList_obj.month,monthPlanList_obj.shopId,monthPlanList_obj.pageSize,
                                    monthPlanList_obj.X_Type)
    #2.4.7.4
    def test_monthPlanDetail(self,monthPlanDetail_obj):
        res = actions.monthPlanDetail(monthPlanDetail_obj.url,monthPlanDetail_obj.planId,monthPlanDetail_obj.X_Type)
    #2.4.8.1
    def test_operationCaseList(self,operationCaseList_obj):
        res = actions.operationCaseList(operationCaseList_obj.url,operationCaseList_obj.shopId,operationCaseList_obj.X_Type)
    #2.4.8.2
    def test_operationCaseDetail(self,operationCaseDetail_obj):
        res = actions.operationCaseDetail(operationCaseDetail_obj.url,operationCaseDetail_obj.shopId,operationCaseDetail_obj.month,
                                          operationCaseDetail_obj.X_Type)
    #************************2.5*******************************
    #2.5.1
    def test_customerList_test(self,customerList_obj):
        res= actions.customerList(customerList_obj.url,customerList_obj.shopId,customerList_obj.pageSize,customerList_obj.X_Type)
    #2.5.2
    def test_customerDetails_test(self,customerDetails_obj):
        res = actions.customerDetails(customerDetails_obj.url,customerDetails_obj.shopId,customerDetails_obj.customerId,
                                      customerDetails_obj.X_Type)
    #2.5.3
    def test_allocationCustomer_test(self,allocationCustomer_obj):
        res = actions.allocationCustomer(allocationCustomer_obj.url,allocationCustomer_obj.shopId,allocationCustomer_obj.personnelId,
                                         allocationCustomer_obj.customerId,allocationCustomer_obj.X_Type)
    #2.5.4
    def test_expenseRecord_test(self,expenseRecord_obj):
        res = actions.expenseRecord(expenseRecord_obj.url,expenseRecord_obj.customerId,expenseRecord_obj.shopId,
                                    expenseRecord_obj.pageSize,expenseRecord_obj.X_Type)


    # 2.5.5
    def test_expenseProject_test(self, expenseProject_obj):
        res = actions.expenseProject(expenseProject_obj.url, expenseProject_obj.customerId, expenseProject_obj.shopId,
                                     expenseProject_obj.pageSize, expenseProject_obj.X_Type)
    #2.5.6
    def test_changeRank_test(self,changeRank_obj):
        res = actions.changeRank(changeRank_obj.url,changeRank_obj.shopId,changeRank_obj.rankId,changeRank_obj.customerIds,
                                 changeRank_obj.X_Type)
    #2.5.7
    def test_rankInfoList_test(self,rankInfoList_obj):
        res = actions.rankInfoList(rankInfoList_obj.url,rankInfoList_obj.shopId,rankInfoList_obj.X_Type)
    #2.5.8.1
    def test_customerCardList(self,customerCardList_obj):
        res = actions.customerCardList(customerCardList_obj.url,customerCardList_obj.shopId,customerCardList_obj.customerId,
                                       customerCardList_obj.pageSize,customerCardList_obj.page,customerCardList_obj.X_Type)
    #2.5.8.2
    def test_cardConsummerDetailList(self, cardConsummerDetailList_obj):
        res = actions.cardConsummerDetailList(cardConsummerDetailList_obj.url, cardConsummerDetailList_obj.cardId,
                                              cardConsummerDetailList_obj.pageSize, cardConsummerDetailList_obj.X_Type)
    # *****************************************2.6*****************************************
    #2.6.1
    def test_findAccountBalance_test(self,findAccountBalance_obj):
        res = actions.findAccountBalance(findAccountBalance_obj.url,findAccountBalance_obj.businessId,
                                         findAccountBalance_obj.X_Type)
    #2.6.2
    def test_accountRecordList_test(self,accountRecordList_obj):
        res = actions.accountRecordList(accountRecordList_obj.url,accountRecordList_obj.businessId,accountRecordList_obj.pageSize,
                                         accountRecordList_obj.X_Type)
    #2.6.3
    def test_putApply_test(self,putApply_obj):
        res = actions.putApply(putApply_obj.url,putApply_obj.businessId,putApply_obj.paymentMode,putApply_obj.price,putApply_obj.X_Type)
    #2.6.4
    def test_putRecordDetail(self,putRecordDetail_obj):
        res = actions.putRecordDetails(putRecordDetail_obj.url,putRecordDetail_obj.id,putRecordDetail_obj.X_Type)
    #2.6.5
    def test_incomeRecordDetail(self,incomeRecordDetail_obj):
        res = actions.incomeRecordDetail(incomeRecordDetail_obj.url,incomeRecordDetail_obj.id,incomeRecordDetail_obj.X_Type)
    # **********************************************2.7*****************************************
    #2.7.1
    def test_shopCapacity(self,shopCapacity_obj):
        res = actions.shopCapacity(shopCapacity_obj.url,shopCapacity_obj.businessId,shopCapacity_obj.shopId,shopCapacity_obj.bunkCount,
                                   shopCapacity_obj.projectAverageDuration,shopCapacity_obj.workStartDate,shopCapacity_obj.workEndDate,
                                   shopCapacity_obj.personnelCount,shopCapacity_obj.customerAverageExpense,
                                   shopCapacity_obj.activeCustomerCount,shopCapacity_obj.mainProjectAverageDuration,shopCapacity_obj.X_Type)
    #2.7.2
    def test_shopDiagnose(self,shopDiagnose_obj):
        res = actions.shopDiagnose(shopDiagnose_obj.url,shopDiagnose_obj.businessId,shopDiagnose_obj.shopId,shopDiagnose_obj.monthShopTurnover,
                                   shopDiagnose_obj.dayShopCustomerCount,shopDiagnose_obj.personnelCount,shopDiagnose_obj.monthTookeenCount,
                                   shopDiagnose_obj.yearShopTurnover)
    #2.7.3
    def test_getShopCapacity(self,getShopCapacity_obj):
        res = actions.getShopCapacity(getShopCapacity_obj.url,getShopCapacity_obj.businessId,getShopCapacity_obj.shopId,
                                      getShopCapacity_obj.X_Type)

    #2.7.4
    def test_getShopDiagnose(self, getShopDiagnose_obj):
        res = actions.getShopDiagnose(getShopDiagnose_obj.url, getShopDiagnose_obj.businessId, getShopDiagnose_obj.shopId,
                                      getShopDiagnose_obj.X_Type)
    #*******************************************************2.8****************************************************************************
    #2.8.1
    def test_createActivity(self,createActivity_obj):
        res = actions.createActivity(createActivity_obj.url,createActivity_obj.businessId,createActivity_obj.shopId,
                                     createActivity_obj.activityName,createActivity_obj.activityStartDate,createActivity_obj.activityEndDate,
                                     createActivity_obj.activityUnitPrice,createActivity_obj.activityCoursePrice,createActivity_obj.description,
                                     createActivity_obj.projectIds,createActivity_obj.X_Type)
    #2.8.2
    def test_activityList(self,activityList_obj):
        res = actions.activityList(activityList_obj.url,activityList_obj.shopId,activityList_obj.pageSize,activityList_obj.X_Type)
    #2.8.3
    def test_activityDetail(self,activityDetail_obj):
        res = actions.activiDetail(activityDetail_obj.url,activityDetail_obj.activityId,activityDetail_obj.shopId,activityDetail_obj.pageSize,
                                   activityDetail_obj.X_Type)
    #2.8.4
    def test_activityQr(self,activityQr_obj):
        res = actions.activityQr(activityQr_obj.url,activityQr_obj.shopId,activityQr_obj.activityId,activityQr_obj.X_Type)
    #2.8.5
    def test_activityPersonnelList(self,activityPersonnelList_obj):
        res = actions.activityPersonnelList(activityPersonnelList_obj.url,activityPersonnelList_obj.activityId,activityPersonnelList_obj.pageSize,
                                            activityPersonnelList_obj.X_Type)
    #2.8.6
    def test_activityChooseProjectList(self,activityChooseProjectList_obj):
        res = actions.activityChooseProjectList(activityChooseProjectList_obj.url,activityChooseProjectList_obj.shopId,
                                                activityChooseProjectList_obj.pageSize,activityChooseProjectList_obj.X_Type)
