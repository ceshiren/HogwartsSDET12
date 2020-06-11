#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWeixin:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "abc"
        caps['udid'] = os.getenv("udid", None)
        # caps["appPackage"] = "com.tencent.wework"
        # caps["appActivity"] = ".launch.WwMainActivity"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['noReset'] = "true"
        # caps['skipServerInstallation'] = True
        # caps['skipDeviceInitialization'] = True
        # caps['dontStopAppOnReset'] = True
        self.driver = webdriver.Remote("http://192.168.56.1:4444/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_case4(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search")

    def test_case5(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search")

    def test_case6(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search")
