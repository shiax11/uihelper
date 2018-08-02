# -*- coding: utf-8 -*-
import sys
import os
import unittest
import traceback
from time import sleep
from uiHelper import UiHelper

class TestCase(unittest.TestCase):
    """第一次使用APP"""

    def TestCase_001(self):
        u"""注册"""
        sleep(3)
        el.localizeId("android:id/button1").click()
        sleep(3)
        el.localizeId("android:id/button1").click()
        sleep(3)
        #注册按键
        el.localizeName("注册").click()
        sleep(1)
        el.localizeName("请输入手机号").send_keys("17311111130")
        sleep(1)
        el.localizeName("获取验证码").click()
        sleep(4)
        el.localizeName("短信验证码").send_keys("8888")
        sleep(1)
        el.localizeId("cn.douyuu.miqu:id/regist_edt_password").send_keys("123456")
        sleep(1)
        el.localizeName("提交").click()
        sleep(5)
        #联系人详情
        #头像
        el.localizeId("cn.douyuu.miqu:id/regist_upload_head").click()
        sleep(1)
        el.localizeId("cn.douyuu.miqu:id/dialog_tv_camera").click()
        sleep(3)
        el.localizeName("确定").click()
        sleep(1)
        el.localizeName("允许").click()
        sleep(1)
        el.localizeName("拍照").click()
        sleep(3)
        el.localizeId("com.android.camera:id/v6_shutter_button_internal").click()
        sleep(3)
        el.localizeId("com.android.camera:id/v6_btn_done").click()
        sleep(1)
        el.localizeId("cn.douyuu.miqu:id/clip_iv_ok").click()
        #昵称
        el.localizeName("1-8个字符").send_keys("shiax11")
        sleep(1)
        el.localizeId("cn.douyuu.miqu:id/regist_rb_wowan").click()
        sleep(1)
        el.localizeId("cn.douyuu.miqu:id/regist_edt_inviteid").send_keys("101003")
        sleep(2)
        el.localizeName("完成").click()
        sleep(15)