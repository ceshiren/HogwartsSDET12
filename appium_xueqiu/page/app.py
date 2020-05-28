from appium import webdriver

from appium_wework.page.base_page import BasePage
from appium_xueqiu.page.main import Main


class App(BasePage):
    def start(self):
        if self._driver == None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps['noReset'] = "true"
            caps['skipServerInstallation'] = True
            caps['skipDeviceInitialization'] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()

        self._driver.implicitly_wait(3)

        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)
