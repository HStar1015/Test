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
