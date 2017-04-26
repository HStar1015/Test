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
    #4.1.9
    def test_miniAppLogin_test(self,miniAppLogin_obj):
        res = actions.miniAppLogin(miniAppLogin_obj.url,miniAppLogin_obj.openId,miniAppLogin_obj.X_Type)
    #****************************************************4.2****************************************************************
    #4.2.1
    def test_projectPersonnelList_test(self,projectPersonnelList_obj):
        res = actions.projectPersonnelList(projectPersonnelList_obj.url,projectPersonnelList_obj.projectId
                                           ,projectPersonnelList_obj.pageSize,projectPersonnelList_obj.X_Type)
    #4.2.2
    def test_personnelProjectList_test(self,personnelProjectList_obj):
        res = actions.personnelProjectList(personnelProjectList_obj.url,personnelProjectList_obj.personnelId,personnelProjectList_obj.pageSize,
                                           personnelProjectList_obj.X_Type)
    #4.2.3
    def test_orderSave_test(self,orderSave_obj):
        res = actions.orderSave(orderSave_obj.url,orderSave_obj.projectId,orderSave_obj.personnelId,orderSave_obj.customerId,
                                orderSave_obj.makeStartDate,orderSave_obj.makeEndDate,orderSave_obj.priceType,orderSave_obj.reserveName,
                                orderSave_obj.reservePhone)
