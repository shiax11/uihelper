# -*- coding: utf-8 -*-
import sys
import os
import unittest
import traceback
from time import sleep
from uiHelper import UiHelper

class LanDing(unittest.TestCase):

    def test001_pe(self):
        #---存储权限---#
        storage = "android:id/button1"
        #-获取手机号码、imei权限-#
        imei = "android:id/button1"
        uiHeloer = UiHelper("deviceConfig.txt")
        uiHeloer.initDriver()
        sleep(3)
        uiHeloer.clickElement(storage)
        sleep(3)
        uiHeloer.clickElement(imei)
        uiHeloer.quitDriver()
    def test02_registered(self):
        # -确定访问权限-#
        AccessAuthority = "android:id/button1"
        # -注册按键-#
        RegistrationButton = "cn.douyuu.miqu:id/loginGuide_register_btn"
        # -手机号输入框-#
        PhoneNumber = "cn.douyuu.miqu:id/regist_edt_phone"
        # -短信输入框-#
        messagecode = "cn.douyuu.miqu:id/regist_edt_messagecode"
        # -获取短信按键-#
        code = "cn.douyuu.miqu:id/regist_tv_get_auth_code"
        # -输入密码输入框-#
        password = "cn.douyuu.miqu:id/regist_edt_password"
        # -密码-#
        protoco2 = "123456"
        # -提交按键-#
        submit = "cn.douyuu.miqu:id/regist_next_step"
        # -协议同意按键-#
        protocol = "cn.douyuu.miqu:id/check_protocol"
        # -查看协议-#
        UserProtocol = "cn.douyuu.miqu:id/tv_user_protocol"
        # -头像-#
        head = "cn.douyuu.miqu:id/regist_upload_head"
        # -昵称-#
        nick = "cn.douyuu.miqu:id/regist_edt_nick"
        # -性别男-#
        man = "cn.douyuu.miqu:id/regist_rb_man"
        # -性别女-#
        wowan = "cn.douyuu.miqu:id/regist_rb_wowan"
        # -邀请人-#
        inviteid = "cn.douyuu.miqu:id/regist_edt_inviteid"
        # -完成-#
        complete = "cn.douyuu.miqu:id/regist_complete"
        # -拍照-#
        camera = "cn.douyuu.miqu:id/dialog_tv_camera"
        # -拍照确定-#
        internal = "com.android.camera:id/v6_shutter_button_internal"
        # -照片二次确认-#
        panel1 = "com.android.camera:id/v6_btn_done"
        panel2 = "com.android.camera:id/v6_btn_cancel"
        # -照片调整-#
        ok = "cn.douyuu.miqu:id/clip_iv_ok"
        de = "cn.douyuu.miqu:id/clip_iv_del"
        # -相册-#
        SelectPic = "cn.douyuu.miqu:id/dialog_tv_select_pic"
        # -系统相册-#
        icon = "相册"
        # -文件管理-#
        icon1 = "文件管理"
        # -获取相机权限,p确定，n取消-#
        camera1 = "cn.douyuu.miqu:id/btn_p"
        camera2 = "cn.douyuu.miqu:id/btn_n"
        # -系统确认访问相机取消,1确定，2取消-#
        button1 = "android:id/button1"
        button2 = "android:id/button2"
        # -完成注册-#
        done = "cn.douyuu.miqu:id/regist_complete"
        uiHeloer = UiHelper("deviceConfig1.txt")
        uiHeloer.initDriver()
        sleep(10)
        try:
            registered = None
            try:
                #-点击注册按键-#
                registered = uiHeloer.findElement(RegistrationButton)
            except:
                uiHeloer.saveScreenshot("没有到登录注册界面.png")
                uiHeloer.initDriver()
                print "没有注册按键"
            registered.click()
            try:
                uiHeloer.waitForElementBySystem(PhoneNumber, 10)
                uiHeloer.clickElement(PhoneNumber)
            except:
                pass
            uiHeloer.findElement(PhoneNumber).set_value("16666666664")
            sleep(3)
            uiHeloer.findElement(messagecode).set_value("8888")
            sleep(3)
            uiHeloer.findElement(code).click()
            sleep(3)
            uiHeloer.findElement(password).set_value(protoco2)
            sleep(3)
            uiHeloer.findElement(submit).click()
            print "手机账号密码填写完成"
            sleep(3)
            uiHeloer.findElement(nick).set_value("1")
            sleep(1)
            uiHeloer.findElement(man).click()
            sleep(1)
            uiHeloer.findElement(head).click()
            sleep(1)
            uiHeloer.findElement(camera).click()
            sleep(1)
            uiHeloer.findElement(camera1).click()
            sleep(1)
            uiHeloer.findElement(AccessAuthority).click()
            sleep(3)
            uiHeloer.findElement(camera).click()
            sleep(3)
            uiHeloer.findElement(internal).click()
            sleep(3)
            uiHeloer.findElement(panel1).click()
            sleep(3)
            uiHeloer.findElement(ok).click()
            sleep(3)
            uiHeloer.findElement(done).click()
            try:
                uiHeloer.waitForElementBySystem("cn.douyuu.miqu:id/tab_hall_top", 10)
            except:
                uiHeloer.saveScreenshot("注册失败.png")
                print "注册失败"
            print "注册完成"
        finally:
            if (uiHeloer != None):
                uiHeloer.quitDriver()
    if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(test02_registered)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def test03_login(self):
        #-登录界面按键-#
        denglu = "cn.douyuu.miqu:id/loginGuide_login_btn"
        #-QQ-#
        qq = "cn.douyuu.miqu:id/loginGuide_shortcut_QQ_iv"
        #-微信-#
        WeChat = "cn.douyuu.miqu:id/loginGuide_shortcut_WX_iv"
        #-ID输入框-#
        ID = "cn.douyuu.miqu:id/login_edt_phone"
        #-密码输入框-#
        password = "cn.douyuu.miqu:id/login_edt_pwd"
        #-忘记密码-#
        passwordS = "cn.douyuu.miqu:id/login_tv_find_password"
        #-登录按键-#
        login = "cn.douyuu.miqu:id/login_tv_login"
        # -密码-#
        protoco2 = "123456"
        uiHeloer = UiHelper("deviceConfig1.txt")
        uiHeloer.initDriver()
        sleep(10)
        try:
            login1 = None
            try:
                login1 = uiHeloer.findElement(denglu)
            except:
                print "没有找到登录按键"
            login1.click()
            sleep(3)
            try:
                uiHeloer.waitForElementBySystem(ID, 10)
            except:
                print "没有到登录界面"
                pass
            uiHeloer.findElement(ID).set_value("16666666664")
            sleep(1)
            uiHeloer.findElement(password).set_value(protoco2)
            sleep(1)
            uiHeloer.clickElement(login)
            try:
                uiHeloer.waitForElementBySystem("cn.douyuu.miqu:id/tab_hall_top", 10)
            except:
                uiHeloer.saveScreenshot("登录失败.png")
                print "登录失败"
                pass
            sleep(3)
            uiHeloer.saveScreenshot("登录成功.png")
            print "登录成功"
        finally:
            if (uiHeloer != None):
                uiHeloer.quitDriver()
    if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(test03_login)
        unittest.TextTestRunner(verbosity=2).run(suite)
