# -*- coding: utf-8 -*-
import actions
class test_core_server():
    #5.1
    def test_authPhone(self,authPhone_obj):
        res = actions.authPhone(authPhone_obj.url,authPhone_obj.type,authPhone_obj.phone,
                                authPhone_obj.operationType)
    #5.2
    def test_authPic(self,authPic_obj):
        res = actions.authPic(authPic_obj.url,authPic_obj.phone)
    #5.3
    def test_projectTypeTree(self,projectTypeTree_obj):
        res = actions.projectTypeTree(projectTypeTree_obj.url)
    #5.4
    def test_message(self,message_obj):
        res = actions.messages(message_obj.url,message_obj.banner,message_obj.platform,message_obj.pageSize)
    #5.5
    def test_rankList(self,rankList_obj):
        res = actions.rankList(rankList_obj.url)