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
    #5.6
    def test_getShareUrl(self,getShareUrl_obj):
        res = actions.getShareUrl(getShareUrl_obj.url,getShareUrl_obj.type,getShareUrl_obj.id)
    #5.7
    def test_findPassword(self,findPassword_obj):
        res = actions.findPassword(findPassword_obj.url,findPassword_obj.authCode,findPassword_obj.type,
                                   findPassword_obj.phone,findPassword_obj.newPassword)
    #5.8
    def test_updatePassword(self,updatePassword_obj):
        res = actions.updatePassword(updatePassword_obj.url,updatePassword_obj.type,updatePassword_obj.phone,
                                     updatePassword_obj.oldPassword,updatePassword_obj.newPassword)
    #5.9
    def test_payMode(self,payMode_obj):
        res = actions.payMode(payMode_obj.url,payMode_obj.type)
    #5.10
    def test_areaList(self,areaList_obj):
        res = actions.areaList(areaList_obj.url,areaList_obj.cityId)
    #5.11
    def test_activityDetail(self,activityDetail_obj):
        res = actions.activityDetail(activityDetail_obj.url, activityDetail_obj.id,activityDetail_obj.userId,
                                 activityDetail_obj.type)
    #5.12
    def test_vote(self,vote_obj):
        res = actions.vote(vote_obj.url,vote_obj.activityId,vote_obj.contentId,vote_obj.phone)
    #5.13
    def test_voteStatical(self,voteStatical_obj):
        res = actions.voteStatical(voteStatical_obj.url,voteStatical_obj.activityId)
    #5.14
    def test_winList(self,winList_obj):
        res = actions.winList(winList_obj.url,winList_obj.activityId)
    #5.15
    def test_peopleVoteStatus(self,peopleVoteStatus_obj):
        res = actions.peopleVoteStatus(peopleVoteStatus_obj.url,peopleVoteStatus_obj.activityId,peopleVoteStatus_obj.phone)
    #5.16
    def test_projectPhoto(self,projectPhoto_obj):
        res = actions.projectPhoto(projectPhoto_obj.url,projectPhoto_obj.groupNo)
    #5.17
    def test_baiduCoordinate(self,baiduCoordinateo_obj):
        res = actions.baiduCoordinate(baiduCoordinateo_obj.url,baiduCoordinateo_obj.latitude,baiduCoordinateo_obj.longitude)
    #5.18
    def test_getOpenId(self,getOpenId_obj):
        res = actions.getOpenId(getOpenId_obj.url,getOpenId_obj.jsCode)
    #5.19
    def test_reservePeriodList(self,reservePeriod_obj):
        res = actions.reservePeriodList(reservePeriod_obj.url)
    #5.20
    def test_reserveTimeList(self,reserveTimeList_obj):
        res = actions.reserveTimeList(reserveTimeList_obj.url,reserveTimeList_obj.personnelId,reserveTimeList_obj.dateTime)
    #5.21
    def test_feedback(self,feedback_obj):
        res = actions.feedback(feedback_obj.url,feedback_obj.userType,feedback_obj.userId,feedback_obj.phone,feedback_obj.name,
                               feedback_obj.content)
    #5.22
    def test_getShareQR(self,getShareQR_obj):
        res = actions.getShareQR(getShareQR_obj.url,getShareQR_obj.personnelId,getShareQR_obj.path,getShareQR_obj.width)

    #5.23
    def test_versionRenewal(self,versionRenewal_obj):
        res = actions.versionRenewal(versionRenewal_obj.url,versionRenewal_obj.os,versionRenewal_obj.port)
    #5.24
    def test_getZoning(self,getZoning_obj):
        res = actions.getZoning(getZoning_obj.url)
    #5.25
    def test_getCitySort(self,getCitySort_obj):
        res = actions.getCitySort(getCitySort_obj.url)
    #5.26
    def test_getBankCardList(self,getBankCardList_obj):
        res = actions.getBankCardList(getBankCardList_obj.url)
