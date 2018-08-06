# -*- coding: utf-8 -*-
import sys
import os
import unittest
import traceback
from time import sleep
from uiHelper import UiHelper

class test01(unittest.TestCase):
    def test04_ResetPasswords(self):
        # -登录按键-#
        login = "cn.douyuu.miqu:id/login_tv_login"
        # -ID输入框-#
        ID = "cn.douyuu.miqu:id/login_edt_phone"
        # -密码输入框-#
        password = "cn.douyuu.miqu:id/login_edt_pwd"
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
                                uiHelper.findElement(phone).set_value("16666666675")
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
                                    uiHelper.findElement(ID).set_value("16666666675")
                                    sleep(1)
                                    uiHelper.findElement(password).set_value(protoco2)
                                    uiHelper.clickElement()
                                    try:
                                        uiHelper.waitForElementBySystem("cn.douyuu.miqu:id/tab_hall_top", 10)
                                        uiHelper.saveScreenshot("G:\uihelper\screenshot\User\est07.png")
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
        suite = unittest.TestLoader().loadTestsFromTestCase(test001_pe)
        unittest.TextTestRunner(verbosity=2).run(suite)