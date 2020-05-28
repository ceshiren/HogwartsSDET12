# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python


"""
改造1： pytest模式
改造2： 改造成可维护的代码形态，绝对不允许有绝对路径的存在 
改造3： 将自动生成的find_element_by_**  改造成find_element(MobileBy.)
改造4： 添加断言 
改造5： 合理使用 setup_class, setup 方法 
"""
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestXueQiu:
    def setup_class(self):
        print("setup_class")
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['noReset'] = "true"
        caps['skipServerInstallation'] = True
        caps['skipDeviceInitialization'] = True

        self.driver = webdriver.Remote("http://localhost:4724/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        print("teardown_class")
        self.driver.quit()

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/action_close').click()

    @pytest.mark.parametrize('searchkey,searchresult', [
        ("alibaba", "阿里巴巴"),
        ("jd", "京东")
    ])
    def test_search(self, searchkey, searchresult):
        print("search")
        el1 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search")
        el1.click()

        el2 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text")
        el2.send_keys(searchkey)

        el3 = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{searchresult}']")
        el3.click()

        el4 = self.driver.find_elements(MobileBy.XPATH,
                                        f"//*[@text='{searchresult}']/../..//*[@text='加自选']")
        if len(el4) > 0:
            el4[0].click()
            self.driver.find_element(MobileBy.XPATH,
                                     f"//*[@text='{searchresult}']/../..//*[@text='已添加']")
        else:
            print("已加自选")

