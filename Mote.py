# -*- coding: utf-8 -*-
import sys
import os
import unittest
import traceback
from time import sleep
from uiHelper import UiHelper

class LanDing(unittest.TestCase):

    def test001_permission(self):
        #---存储权限---#
        storage = "android:id/button1"
        #-获取手机号码、imei权限-#
        imei = "android:id/button1"
        uiHeloer = UiHelper("deviceConfig.txt")
        uiHeloer.initDriver()
        sleep(3)
        uiHeloer.findElement(storage).click()
        sleep(3)
        uiHeloer.findElement(imei).click()
        print "获取权限成功"
        sleep(3)

    def test02_registered(self):
        #-注册按键-#
        RegistrationButton = "cn.douyuu.miqu:id/loginGuide_register_btn"
        #-手机号输入框-#
        PhoneNumber = "cn.douyuu.miqu:id/regist_edt_phone"
        #-短信输入框-#
        messagecode = "cn.douyuu.miqu:id/regist_edt_messagecode"
        #-获取短信按键-#
        code = "cn.douyuu.miqu:id/regist_tv_get_auth_code"
        #-输入密码输入框-#
        password = "cn.douyuu.miqu:id/regist_edt_password"
        # -密码-#
        protoco2 = "123456"
        #-提交按键-#
        submit = "cn.douyuu.miqu:id/regist_next_step"
        #-协议同意按键-#
        protocol = "cn.douyuu.miqu:id/check_protocol"
        #-查看协议-#
        UserProtocol = "cn.douyuu.miqu:id/tv_user_protocol"
        #-头像-#
        head = "cn.douyuu.miqu:id/regist_upload_head"
        #-昵称-#
        nick = "cn.douyuu.miqu:id/regist_edt_nick"
        #-性别男-#
        man = "cn.douyuu.miqu:id/regist_rb_man"
        #-性别女-#
        wowan = "cn.douyuu.miqu:id/regist_rb_wowan"
        #-邀请人-#
        inviteid = "cn.douyuu.miqu:id/regist_edt_inviteid"
        #-完成-#
        complete = "cn.douyuu.miqu:id/regist_complete"
        #-拍照-#
        camera = "cn.douyuu.miqu:id/dialog_tv_camera"
        #-拍照确定-#
        internal = "com.android.camera:id/v6_shutter_button_internal"
        #-照片选择或者取消-#
        panel1 = "com.android.camera:id/capture_control_panel"
        panel2 = "com.android.camera:id/v6_btn_cancel"
        #-照片调整-#
        ok = "cn.douyuu.miqu:id/clip_iv_ok"
        de = "cn.douyuu.miqu:id/clip_iv_del"
        #-相册-#
        SelectPic = "cn.douyuu.miqu:id/dialog_tv_select_pic"
        #-系统相册-#
        icon = "相册"
        #-文件管理-#
        icon1 ="文件管理"
        #-获取相机权限,p确定，n取消-#
        camera1 = "cn.douyuu.miqu:id/btn_p"
        camera2 = "cn.douyuu.miqu:id/btn_n"
        #-系统确认访问相机取消,1确定，2取消-#
        button1 = "android:id/button1"
        button2 = "android:id/button2"

        uiHeloer = UiHelper("deviceConfig1.txt")
        uiHeloer.initDriver()
        uiHeloer.findElement(RegistrationButton).click()
        sleep(1)
        uiHeloer.findElement(PhoneNumber).send_keys("16666666666")
        sleep(1)
        uiHeloer.findElement(messagecode).send_keys("8888")
        sleep(1)
        uiHeloer.findElement(code).click()
        sleep(1)
        uiHeloer.findElement(password).send_keys(protoco2)
        sleep(1)
        uiHeloer.findElement(submit).click()
        print "手机账号密码填写完成"
        sleep(3)
        uiHeloer.findElement(nick).send_keys("1")
        sleep(1)
        uiHeloer.findElement(man).click()
        sleep(1)
        uiHeloer.findElement(head).click()
        sleep(1)
        uiHeloer.findElement(camera).click()
        sleep(1)
        uiHeloer.findElement(camera1).click()
        sleep(1)
        uiHeloer.findElement(camera).click()
        sleep(1)
        uiHeloer.findElement(internal).click()
        sleep(1)
        uiHeloer.findElement(panel1).click()
        sleep(1)
        uiHeloer.findElement(ok).click()
        sleep(1)
        uiHeloer.findElement()