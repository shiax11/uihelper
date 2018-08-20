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




class account(unittest.TestCase):

    def test_login(self):
        #---存储权限---#
        storage = "android:id/button1"
        #-获取手机号码、imei权限-#
        imei = "android:id/button1"
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
        #-创建房间按键-#
        nvb_icon_zbo = "cn.douyuu.miqu:drawable/nvb_icon_zbo"
        #-房间列表-#
        title = "cn.douyuu.miqu:id/tv_title"
        #-登陆界面-#
        tes = "cn.douyuu.miqu:id/middle_text"
        u'''登陆测试'''
        # 要读取的scv文件路径
        my_file = 'D:\\user.csv'
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
            sleep(3)
            uiHeloer.clickElement(denglu)
            sleep(2)
            uiHeloer.findElement(ID).set_value(user[1])
            sleep(1)
            uiHeloer.findElement(password).set_value(user[2])
            sleep(1)
            uiHeloer.clickElement(login)
            sleep(10)
            print ('\n' + '测试项：' + user[6])
            uiHeloer.saveScreenshot(path + user[4] + ".png")
            print user[5]
            assert uiHeloer.findElement(user[7]).text
            try:
                error_message = uiHeloer.findElement(user[7]).text
                self.assertEqual(error_message, user[5])
                print(u'提示信息正确！预期值与实际值一致:')
                print(u'预期值：' + user[5])
                print(u'实际值:' + error_message)
            except:
                print (u'提示信息错误！预期值与实际值不符：')
                print (u'预期值：' + user[5])
                print(u'实际值:' + error_message)
            uiHeloer.quitDriver()

    def test_registered(self):
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
            uiHeloer.clickElement("cn.douyuu.miqu:id/regist_next_step")
            sleep(5)
            print ('\n' + '测试项：' + user[7])
            uiHeloer.saveScreenshot(path + user[5] + ".png")
            assert uiHeloer.findElement(user[8]).text
            try:
                error_me = uiHeloer.findElement(user[8]).text
                self.assertEqual(error_me, user[6])
                print(u'提示信息正确！预期值与实际值一致:')
                print(u'预期值：' + user[6])
                print(u'实际值:' + error_me)
                assert uiHeloer.findElement(user[10]).text
                try:
                    error_message1 = uiHeloer.findElement(user[10]).text
                    self.assertEqual(error_message1, user[9])
                    print(u'提示信息正确！预期值与实际值一致:')
                    print(u'预期值：' + user[9])
                    print(u'实际值:' + error_message1)
                    uiHeloer.findElement(nick).set_value(user[11])
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
                    sleep(5)
                    uiHeloer.clickElement(internal)
                    sleep(5)
                    uiHeloer.clickElement(panel1)
                    sleep(3)
                    uiHeloer.clickElement(ok)
                    sleep(3)
                    uiHeloer.clickElement(done)
                    sleep(10)
                    assert uiHeloer.findElement(user[12]).text
                    try:
                        error_message2 = uiHeloer.findElement(user[12]).text
                        self.assertEqual(error_message2, user[13])
                        print(u'提示信息正确！预期值与实际值一致:')
                        print(u'预期值：' + user[13])
                        print(u'实际值:' + error_message2)
                    except:
                        print (u'没有新手奖励：')
                        print (u'预期值：' + user[13])
                        print(u'实际值:' + error_message2)
                except:
                    print (u'提示信息错误！预期值与实际值不符：')
                    print (u'预期值：' + user[9])
                    print(u'实际值:' + error_message1)
            except:
                print (u'提示信息错误！预期值与实际值不符：')
                print (u'预期值：' + user[6])
                print(u'实际值:' + error_me)
            uiHeloer.quitDriver()


if __name__ == '__main__':
    # 导入HTMLTestRunner库，这句也可以放在脚本开头


    # 定义脚本标题，加u为了防止中文乱码
    report_title = u'蜜趣登陆模块测试报告'

    # 定义脚本内容，加u为了防止中文乱码
    desc = u'登陆模块测试报告详情：'

    # 定义date为日期，time为时间
    date = time.strftime("%Y%m%d")
    time = time.strftime("%Y%m%d%H%M%S")

    # 定义path为文件路径，目录级别，可根据实际情况自定义修改
    path = 'D:/Python_test/' + date + "/login/" + time + "/"

    # 定义报告文件路径和名字，路径为前面定义的path，名字为report（可自定义），格式为.html
    report_path = path + "report.html"

    # 判断是否定义的路径目录存在，不能存在则创建
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass

    # 定义一个测试容器
    testsuite = unittest.TestSuite()

    # 将测试用例添加到容器
    testsuite.addTest(test("test_login"))
    testsuite.addTest(test("test_registered"))
    # 将运行结果保存到report，名字为定义的路径和文件名，运行脚本
    with open(report_path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)

    # 关闭report，脚本结束
    report.close()
    # # 关闭APP
    #uiHeloer.quitDriver()
