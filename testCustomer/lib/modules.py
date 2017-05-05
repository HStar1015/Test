# -*- coding: utf-8 -*-
import actions
class test_core_server():
    # ************************4.1*******************************
    # 4.1.1
    def test_register_test(self, register_obj):
        res = actions.register(register_obj.url,register_obj.phone,register_obj.password,register_obj.authCode,
                                    register_obj.X_Type)

    #4.1.2
    def test_login_test(self,login_obj):
        res = actions.login(login_obj.url,login_obj.phone,login_obj.password,login_obj.X_Type)
    #4.1.3
    def test_updateInfo_test(self,updateInfo_obj):
        res = actions.updateInfo(updateInfo_obj.url,updateInfo_obj.id,updateInfo_obj.files,updateInfo_obj.X_Type)
    #4.1.4
    def test_customerInfo_test(self,customerInfo_obj):
        res = actions.customerInfo(customerInfo_obj.url,customerInfo_obj.id,customerInfo_obj.X_Type)
    #4.1.5
    def test_collectProject_test(self,collectProject_obj):
        res = actions.collectProject(collectProject_obj.url,collectProject_obj.customerId,collectProject_obj.projectId,
                                     collectProject_obj.ifCollect,collectProject_obj.X_Type)
    #4.1.6
    def test_collectProjectList_test(self,collectProjectList_obj):
        res = actions.collectProjectList(collectProjectList_obj.url,collectProjectList_obj.customerId,collectProjectList_obj.longitude,
                                         collectProjectList_obj.latitude,collectProjectList_obj.pageSize,collectProjectList_obj.X_Type)
    #4.1.7
    def test_collectPersonnel_test(self,collectPersonnel_obj):
        res = actions.collectPersonnel(collectPersonnel_obj.url,collectPersonnel_obj.customerId,collectPersonnel_obj.personnelId,
                                       collectPersonnel_obj.ifCollect,collectPersonnel_obj.X_Type)
    #4.1.8
    def test_collectPersonneList_test(self,collectPersonneListt_obj):
        res = actions.collectProjectList(collectPersonneListt_obj.url,collectPersonneListt_obj.customerId,collectPersonneListt_obj.longitude,
                                         collectPersonneListt_obj.latitude,collectPersonneListt_obj.pageSize,collectPersonneListt_obj.X_Type)
    # #4.1.9
    # def test_miniAppLogin_test(self,miniAppLogin_obj):
    #     res = actions.miniAppLogin(miniAppLogin_obj.url,miniAppLogin_obj.openId,miniAppLogin_obj.X_Type)
    #****************************************************4.2****************************************************************
    #4.2.1
    def test_projectPersonnelList_test(self,projectPersonnelList_obj):
        res = actions.projectPersonnelList(projectPersonnelList_obj.url,projectPersonnelList_obj.projectId
                                           ,projectPersonnelList_obj.pageSize,projectPersonnelList_obj.X_Type)
    #4.2.2
    def test_searchPersonnelList_test(self,searchPersonnelList_obj):
        res = actions.searchProjectList(searchPersonnelList_obj.url,searchPersonnelList_obj.personnelId,searchPersonnelList_obj.pageSize,
                                        searchPersonnelList_obj.X_Type)
    #4.2.3
    def test_orderSave_test(self,orderSave_obj):
        res = actions.orderSave(orderSave_obj.url,orderSave_obj.projectId,orderSave_obj.personnelId,orderSave_obj.customerId,
                                orderSave_obj.makeStartDate,orderSave_obj.makeEndDate,orderSave_obj.priceType,orderSave_obj.reserveName,
                                orderSave_obj.reservePhone)
    #4.2.4
    def test_cancelOrder_test(self,cancelOrder_obj):
        res = actions.cancelOrder(cancelOrder_obj.url,cancelOrder_obj.orderNo,cancelOrder_obj.customerId,cancelOrder_obj.X_Type)
    #4.2.5
    def test_applyCancelOrder_test(self,applyCancelOrder_obj):
        res = actions.applyCancelOrder(applyCancelOrder_obj.url,applyCancelOrder_obj.orderNo,applyCancelOrder_obj.customerId,applyCancelOrder_obj)
    #4.2.5
    def test_personnelServeProject_test(self,personnelServeProject_obj):
        res = actions.personnelServeProject(personnelServeProject_obj.url,personnelServeProject_obj.projectId,personnelServeProject_obj.personnelId,
                                            personnelServeProject_obj.X_Type)
    #***************************************4.3****************************************************
    #4.3.1.1
    def test_hotProject_test(self,hotProject_obj):
        res = actions.hotProject(hotProject_obj.url,hotProject_obj.longitude,hotProject_obj.latitude,hotProject_obj.cityId,
                                 hotProject_obj.pageSize,hotProject_obj.X_Type)
    #4.3.1.2
    def test_searchProjectList_test(self,searchProjectList_obj):
        res = actions.searchProjectList(searchProjectList_obj.url,searchProjectList_obj.cityId,searchProjectList_obj.longitude,searchProjectList_obj.latitude,
                                 searchProjectList_obj.page,searchProjectList_obj.pageSize,searchProjectList_obj.X_Type)
    #4.3.1.3
    def test_projectDetails_test(self,projectDetails_obj):
        res = actions.projectDetails(projectDetails_obj.url,projectDetails_obj.id,projectDetails_obj.X_Type)
    #4.3.1.4
    def test_projectCommentGroupNum_test(self,projectCommentGroupNum_obj):
        res = actions.projectCommentGroupNum(projectCommentGroupNum_obj.url,projectCommentGroupNum_obj.projectId,projectCommentGroupNum_obj.X_Type)
    #4.3.1.5
    def test_projectCommentList_test(self,projectCommentList_obj):
        res = actions.projectCommentList(projectCommentList_obj.url,projectCommentList_obj.projectId,projectCommentList_obj.commentLevel,
                                         projectCommentList_obj.pageSize)
    #4.3.2.1
    def test_hotPersonnel_test(self,hotPersonnel_obj):
        res = actions.hotPersonnel(hotPersonnel_obj.url,hotPersonnel_obj.longitude,hotPersonnel_obj.latitude,hotPersonnel_obj.cityId,
                                   hotPersonnel_obj.pageSize,hotPersonnel_obj.X_Type)
    #4.3.2.2
    def test_searchPersonnelList_test(self,searchPersonnelList_obj):
        res = actions.searchPersonnelList(searchPersonnelList_obj.url,searchPersonnelList_obj.cityId,searchPersonnelList_obj.longitude,searchPersonnelList_obj.latitude,
                                          searchPersonnelList_obj.pageSize,searchPersonnelList_obj.X_Type)
    #4.3.2.3
    def test_personnelDetail_test(self,personnelDetail_obj):
        res = actions.personnelDetail(personnelDetail_obj.url,personnelDetail_obj.id,personnelDetail_obj.X_Type)
    #4.3.2.4
    def test_personnelProjectList_test(self,personnelProjectList_obj):
        res = actions.personnelProjectList(personnelProjectList_obj.url,personnelProjectList_obj.shopId,personnelProjectList_obj.personnelId,
                                           personnelProjectList_obj.pageSize)
    #4.3.2.5
    def test_personnelCommentGroupNum_test(self,personnelCommentGroupNum_obj):
        res  = actions.personnelCommentGroupNum(personnelCommentGroupNum_obj.url,personnelCommentGroupNum_obj.personnelId,
                                                personnelCommentGroupNum_obj.X_Type)
    #4.3.2.6
    def test_personnelCommentList_test(self,personnelCommentList_obj):
        res = actions.personnelCommentList(personnelCommentList_obj.url,personnelCommentList_obj.personnelId,
                                           personnelCommentList_obj.commentLevel,personnelCommentList_obj.pageSize,
                                           personnelCommentList_obj.X_Type)
    #************************************************4.4*****************************************************************************
    #4.4.1
    def test_reserveProjectRecord(self,reserveProjectRecord_obj):
        res = actions.reserveProjectRecord(reserveProjectRecord_obj.url,reserveProjectRecord_obj.customerId,reserveProjectRecord_obj.longitude,
                                           reserveProjectRecord_obj.latitude,reserveProjectRecord_obj.pageSize,reserveProjectRecord_obj.X_Type)
    #4.4.2
    def test_reservePersonnelRecord(self,reservePersonnelRecord_obj):
        res = actions.reservePersonnelRecord(reservePersonnelRecord_obj.url,reservePersonnelRecord_obj.customerId,reservePersonnelRecord_obj.longitude,
                                             reservePersonnelRecord_obj.latitude,reservePersonnelRecord_obj.pageSize,reservePersonnelRecord_obj.X_Type)
    #4.4.3
    def test_orderGroupNum(self,orderGroupNum_obj):
        res = actions.orderGroupNum(orderGroupNum_obj.url,orderGroupNum_obj.customerId,orderGroupNum_obj.X_Type)
    #4.4.4
    def test_myOrderList(self,myOderList_obj):
        res = actions.myOrderList(myOderList_obj.url,myOderList_obj.X_Type,myOderList_obj.customerId,myOderList_obj.approveStatus,
                                  myOderList_obj.pageSize)
    #4.4.5
    def test_orderDetail(self,orderDetail_obj):
        res = actions.orderDetail(orderDetail_obj.url,orderDetail_obj.customerId,orderDetail_obj.orderNo,orderDetail_obj.X_Type)
    #4.4.6
    def test_payQRDetail(self,payQRDetail_obj):
        res = actions.payQRDetail(payQRDetail_obj.url,payQRDetail_obj.customerId,payQRDetail_obj.orderNo,payQRDetail_obj.X_Type)
    #4.4.7
    def test_orderComment(self,orderComment_obj):
        res = actions.orderComment(orderComment_obj.url,orderComment_obj.orderNo,orderComment_obj.customerId,orderComment_obj.personnelId,
                                   orderComment_obj.projectId,orderComment_obj.content,orderComment_obj.domainLevel,orderComment_obj.serveLevel,
                                   orderComment_obj.communicationLevel,orderComment_obj.X_Type)
    #4.4.8
    def test_confirmFinishOrder(self,confirmFinishOrder_obj):
        res = actions.confirmFinishOrder(confirmFinishOrder_obj.url,confirmFinishOrder_obj.personnelId,confirmFinishOrder_obj.orderNo,
                                         confirmFinishOrder_obj.X_Type)
    #*************************************4.5************************************************
    #4.5.1
    def test_wechatSubmitPay(self,wechatSubmitPay_obj):
        res = actions.wechatSubmitPay(wechatSubmitPay_obj.url,wechatSubmitPay_obj.openId,wechatSubmitPay_obj.customerId,wechatSubmitPay_obj.orderNo,
                                      wechatSubmitPay_obj.paymentMode,wechatSubmitPay_obj.X_Type)
    #4.5.2
    def test_appSubmitPay(self,appSubmitPay_obj):
        res = actions.appSubmitPay(appSubmitPay_obj.url,appSubmitPay_obj.customerId,appSubmitPay_obj.orderNo,
                                   appSubmitPay_obj.paymentMode,appSubmitPay_obj.X_Type)
    #4.5.3
    def test_checkOrderPayStatus(self,checkOrderPayStatus_obj):
        res = actions.checkOrderPayStatus(checkOrderPayStatus_obj.url,checkOrderPayStatus_obj.customerId,checkOrderPayStatus_obj.orderNo,
                                   checkOrderPayStatus_obj.X_Type)