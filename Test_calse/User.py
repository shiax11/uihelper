# -*- coding: utf-8 -*-
import sys
import os
import unittest
import traceback
from time import sleep
from uiHelper import UiHelper

class UserAccount(unittest.TestCase):

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
                registered = uiHeloer.clickElement(RegistrationButton)

                try:
                    uiHeloer.waitForElementBySystem(PhoneNumber, 10)
                    uiHeloer.clickElement(PhoneNumber)
                    uiHeloer.findElement(PhoneNumber).set_value("16644666671")
                    sleep(3)
                    uiHeloer.findElement(messagecode).set_value("8888")
                    sleep(3)
                    uiHeloer.clickElement(code)
                    sleep(3)
                    uiHeloer.findElement(password).set_value(protoco2)
                    sleep(3)
                    uiHeloer.clickElement(submit)
                    sleep(3)
                    try:
                        uiHeloer.waitForElementBySystem(UserProtocol, 10)
                        uiHeloer.findElement(nick).set_value("1")
                        sleep(1)
                        uiHeloer.clickElement(man)
                        sleep(1)
                        uiHeloer.clickElement(head)
                        sleep(1)
                        uiHeloer.clickElement(camera)
                        sleep(1)
                        uiHeloer.clickElement(camera1)
                        sleep(1)
                        uiHeloer.clickElement(AccessAuthority)
                        sleep(3)
                        uiHeloer.clickElement(camera)
                        sleep(3)
                        uiHeloer.clickElement(internal)
                        sleep(3)
                        uiHeloer.clickElement(panel1)
                        sleep(3)
                        uiHeloer.clickElement(ok)
                        sleep(3)
                        uiHeloer.clickElement(done)
                        try:
                            uiHeloer.waitForElementBySystem("cn.douyuu.miqu:id/tab_hall_top", 10)
                            sleep(10)
                            uiHeloer.saveScreenshot("G:\uihelper\screenshot\User\est01.png")
                            print "注册完成"
                        except:
                            uiHeloer.saveScreenshot("G:\uihelper\screenshot\User\没有到登录界面.png")
                            print "注册失败"
                    except:
                        uiHeloer.saveScreenshot("G:\uihelper\screenshot\User\输入个人信息界面.png")
                        print "没有到注册界面"
                except:
                    pass
            except:
                uiHeloer.saveScreenshot("G:\uihelper\screenshot\User\没有注册按键.png")
                print "没有注册按键"
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
        #-导航栏-#
        tab4 = "cn.douyuu.miqu:id/tab_imageview4"
        #-设置按键-#
        set = "cn.douyuu.miqu:id/tab_mine_tv_set"
        #-退出登陆-#
        exit_login = "cn.douyuu.miqu:id/tv_exit_login"
        #-退出登陆按键-#
        exit_ok = "cn.douyuu.miqu:id/btn_p"
        uiHeloer = UiHelper("deviceConfig1.txt")
        uiHeloer.initDriver()
        sleep(10)
        try:
            login1 = None
            try:
                login1 = uiHeloer.waitForElementBySystem("cn.douyuu.miqu:id/tab_hall_top", 10)
                uiHeloer.clickElement(tab4)
                sleep(1)
                uiHeloer.swipe(750, 1300, 800, 300, 300)
                sleep(3)
                uiHeloer.clickElement(set)
                sleep(3)
                uiHeloer.swipe(750, 1300, 800, 300, 300)
                sleep(3)
                uiHeloer.clickElement(exit_login)
                sleep(3)
                try:
                    uiHeloer.waitForElementBySystem(exit_ok, 3)
                    uiHeloer.clickElement(exit_ok)
                    sleep(5)
                    uiHeloer.clickElement(denglu)
                    sleep(3)
                    try:
                        uiHeloer.waitForElementBySystem(ID, 10)
                        uiHeloer.findElement(ID).set_value("16644666671")
                        sleep(1)
                        uiHeloer.findElement(password).set_value(protoco2)
                        sleep(1)
                        uiHeloer.clickElement(login)
                        try:
                            uiHeloer.waitForElementBySystem("cn.douyuu.miqu:id/tab_hall_top", 10)
                            sleep(3)
                            uiHeloer.saveScreenshot("G:\uihelper\screenshot\User\est02.png")
                            print "登录成功"
                        except:
                            uiHeloer.saveScreenshot("G:\uihelper\screenshot\User\登录失败.png")
                            print "登录失败"
                            pass
                    except:
                        print "没有到登录界面"
                        pass
                except:
                    print "没有找到登录按键"
                    pass
            except:
                print "没有找到设置界面"
                pass
        finally:
            if (uiHeloer != None):
                uiHeloer.quitDriver()
    if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(test03_login)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def test04_ResetPasswords(self):
        # -登录按键-#
        login = "cn.douyuu.miqu:id/login_tv_login"
        # -ID输入框-#
        ID = "cn.douyuu.miqu:id/login_edt_phone"
        # -密码输入框-#
        password2 = "cn.douyuu.miqu:id/login_edt_pwd"
        # -登录界面按键-#
        denglu = "cn.douyuu.miqu:id/loginGuide_login_btn"
        # -忘记密码-#
        passwordS = "cn.douyuu.miqu:id/login_tv_find_password"
        # -手机号-#
        phone = "cn.douyuu.miqu:id/findpwd_edt_phone"
        # -短信验证码获取按键-#
        code = "cn.douyuu.miqu:id/findpwd_tv_get_auth_code"
        # -短信验证码输入框-#
        note = "cn.douyuu.miqu:id/findpwd_edt_messagecode"
        note1 = "8888"
        # -密码-#
        password = "cn.douyuu.miqu:id/findpwd_edt_password"
        # -密码二次确认-#
        password1 = "cn.douyuu.miqu:id/findpwd_edt_password_again"
        # -确定-#
        ok = "cn.douyuu.miqu:id/findpwd_modify"
        # -导航栏-#
        tab4 = "cn.douyuu.miqu:id/tab_imageview4"
        # -设置按键-#
        set = "cn.douyuu.miqu:id/tab_mine_tv_set"
        # -退出登陆-#
        exit_login = "cn.douyuu.miqu:id/tv_exit_login"
        # -退出登陆按键-#
        exit_ok = "cn.douyuu.miqu:id/btn_p"
        protoco2 = "654321"
        uiHelper = UiHelper("deviceConfig1.txt")
        uiHelper.initDriver()
        sleep(10)
        try:
            denlu = None
            try:
                uiHelper.waitForElementBySystem("cn.douyuu.miqu:id/tab_hall_top", 10)
                uiHelper.clickElement(tab4)
                sleep(1)
                uiHelper.swipe(750, 1300, 800, 300, 300)
                sleep(5)
                uiHelper.clickElement(set)
                sleep(3)
                uiHelper.swipe(750, 1300, 800, 300, 300)
                sleep(3)
                uiHelper.clickElement(exit_login)
                sleep(3)
                try:
                    uiHelper.waitForElementBySystem(exit_ok, 3)
                    uiHelper.clickElement(exit_ok)
                    sleep(5)
                    try:
                        uiHelper.waitForElementBySystem(denglu, 2)
                        uiHelper.clickElement(denglu)
                        sleep(10)
                        uiHelper.saveScreenshot("G:\uihelper\screenshot\User\est03.png")
                        try:
                            uiHelper.waitForElementBySystem(passwordS, 5)
                            uiHelper.saveScreenshot("G:\uihelper\screenshot\User\est04.png")
                            uiHelper.clickElement(passwordS)
                            try:
                                uiHelper.waitForElementBySystem(phone, 1)
                                uiHelper.saveScreenshot("G:\uihelper\screenshot\User\est05.png")
                                sleep(3)
                                uiHelper.findElement(phone).set_value("16644666671")
                                sleep(1)
                                uiHelper.findElement(note).set_value(note1)
                                sleep(1)
                                uiHelper.clickElement(code)
                                sleep(1)
                                uiHelper.findElement(password).set_value(protoco2)
                                sleep(1)
                                uiHelper.findElement(password1).set_value(protoco2)
                                sleep(1)
                                uiHelper.clickElement(ok)
                                try:
                                    uiHelper.waitForElementBySystem(ID, 10)
                                    uiHelper.saveScreenshot("G:\uihelper\screenshot\User\est06.png")
                                    uiHelper.findElement(ID).set_value("16644666671")
                                    sleep(1)
                                    uiHelper.findElement(password2).set_value(protoco2)
                                    sleep(3)
                                    uiHelper.clickElement(login)
                                    try:
                                        uiHelper.waitForElementBySystem("cn.douyuu.miqu:id/tab_hall_top", 10)
                                        uiHelper.saveScreenshot("G:\uihelper\screenshot\User\est07.png")
                                        print "密码找回成功！"
                                    except:
                                        uiHelper.saveScreenshot("G:\uihelper\screenshot\User\密码更改失败.png")
                                        print "密码更改失败"
                                except:
                                    uiHelper.saveScreenshot("G:\uihelper\screenshot\User\找回密码失败.png")
                                    pass
                            except:
                                uiHelper.saveScreenshot("G:\uihelper\screenshot\User\没有到重置密码界面.png")
                                print "没有但重置密码界面"
                                pass
                        except:
                            uiHelper.saveScreenshot("G:\uihelper\screenshot\User\没有到登录界面.png")
                            pass
                    except:
                        uiHelper.saveScreenshot("G:\uihelper\screenshot\User\没有找到登陆按键.png")
                        print "没有找到登陆按键"
                        pass
                except:
                    print "没有找到退出登陆按键"
                    pass
            except:
                print "没有找到设置按键"
                pass
        finally:
            if (uiHelper != None):
                uiHelper.quitDriver()


    if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(test04_ResetPasswords)
        unittest.TextTestRunner(verbosity=2).run(suite)
