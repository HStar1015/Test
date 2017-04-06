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
