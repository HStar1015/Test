# -*- coding: utf-8 -*-
import actions
class test_core_server():
    # ************************4.1*******************************
    # 4.1.1
    def test_register_test(self, register_obj):
        res = actions.register(register_obj.url,register_obj.phone,register_obj.password,register_obj.authCode,
                                    register_obj.X_Type)

    #3.1.2
    def test_login_test(self,login_obj):
        res = actions.login(login_obj.url,login_obj.phone,login_obj.password,login_obj.X_Type)
