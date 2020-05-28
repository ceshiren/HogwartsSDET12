#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

import pytest
from appium_wework import webdriver
from appium_wework.webdriver.common.mobileby import MobileBy


class TestTransaction():
    def setup(self):
        desire_cap = {
            "platformName": "Android",
            "deviceName": "7XBNW19910007839",
            "appPackage": "com.bkt.exchange",
            "appActivity": ".activity.StartPageActivity",
            "autoGrantPermissions" : True,
            # 支持中文输入
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true",
            # 绕过弹窗
            "noReset": True,
            # 不需要重启，直接按照上次停留的页面继续操作（提升运行速度）
            # "dontStopAppOnReset": True,
            # 跳过安装，权限等设置等操作（提升运行速度）
            "skipDeviceInitialization": True
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        sleep(2)
        self.driver.quit()
        pass

    def test_search(self):
        print("这是一个搜索案例")
        sleep(3)
        self.driver.find_element(MobileBy.XPATH,
                                 f"//*[@resource-id='com.bkt.exchange:id/tv_indicator'and @text='交易']").click()
        self.driver.find_element(MobileBy.CLASS_NAME, "android.widget.ImageView").click()

    @pytest.mark.parametrize("cointype,result",[
        ('BKK',"BKK/USDT"),
        ('BNB',"BNB/USDT")
    ])
    def test_bkk(self,cointype,result):
        # self.driver.find_element(MobileBy.ID, "com.bkt.exchange:id/stv_search").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='交易']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.bkt.exchange:id/rightContainLin']/android.widget.ImageView").click()
        self.driver.find_element(MobileBy.ID, "com.bkt.exchange:id/coin_edit").send_keys(cointype)
        self.driver.find_element(MobileBy.XPATH, f"//*[@resource-id='com.bkt.exchange:id/pair' and @text='{result}']").click()

    #     self.driver.find_element(MobileBy.ID, "com.bkt.exchange:id/coin_edit").send_keys(cointype)
    #     sleep(3)
    # # @pytest.mark.parametrize("transtype",['BKK/USDT','BNB/USDT','ETH/SUDT'])
    # # def test_response(self,transtype):
    #     self.driver.find_element(MobileBy.XPATH,
    #                                    f"//*[@resource-id='com.bkt.exchange:id/pair] and @text='{cointype}").click()
    #     sleep(2)
    #     # 返回到上一页面
    #     self.driver.back()
        # self.driver.back()
    #
    # def test_add_favorites(self):
    #     pass
if __name__ == '__main__':
    pytest.main()