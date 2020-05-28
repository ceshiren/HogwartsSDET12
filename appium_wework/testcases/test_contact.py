from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWeixin:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps['noReset'] = "true"
        caps['skipServerInstallation'] = True
        caps['skipDeviceInitialization'] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_addcontact(self):
        print("添加联系人")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        nameelement = self.driver.find_element(MobileBy.XPATH,
                                               "//*[@text='姓名　']/..//*[@class='android.widget.EditText']")
        nameelement.send_keys("霍格name1")
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='性别']/..//*[contains(@class, 'TextView') and @text='男']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        phonenum_element = self.driver.find_element(MobileBy.XPATH,
                                                    "//*[@text='手机　']/..//*[contains(@class, 'EditText')]")
        phonenum_element.send_keys("18712345678")

        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gur").click()
        sleep(1)
        print(self.driver.page_source)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")
