# -*- coding: utf-8 -*-

import csv  # 导入scv库，可以读取csv文件
import unittest
from time import sleep
import time
import os
from uiHelper import UiHelper
from HTMLTestRunner import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# ---存储权限---#
storage = "android:id/button1"
#     #-获取手机号码、imei权限-#
imei = "android:id/button1"
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
sub = "cn.douyuu.miqu:id/regist_next_step"
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
my_file = 'D:\\login1.csv'
        # csv.reader()读取csv文件，
        # Python3.X用open，Python2.X用file，'r'为读取
        # open(file,'r')中'r'为读取权限，w为写入，还有rb，wd等涉及到编码的读写属性
data = csv.reader(open(my_file, 'r'))
        # for循环将读取到的csv文件的内容一行行循环，这里定义了user变量(可自定义)
        # user[0]表示csv文件的第一列，user[1]表示第二列，user[N]表示第N列
        # for循环有个缺点，就是一旦遇到错误，循环就停止，所以用try，except保证循环执行完

for user in data:
    uiHeloer = UiHelper("deviceConfig.txt")
    uiHeloer.initDriver()
    sleep(10)
    uiHeloer.clickElement(storage)
    sleep(3)
    uiHeloer.clickElement(imei)
    sleep(5)
    uiHeloer.clickElement(RegistrationButton)
    sleep(3)
    uiHeloer.findElement(PhoneNumber).set_value(user[1])
    sleep(1)
    uiHeloer.findElement(password).set_value(user[2])
    sleep(1)
    uiHeloer.findElement(messagecode).set_value(user[3])
    sleep(1)
    uiHeloer.clickElement(code)
    sleep(3)
    uiHeloer.clickElement(sub)
    sleep(5)