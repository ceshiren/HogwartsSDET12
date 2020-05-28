from selenium.webdriver.common.by import By

from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self._driver.implicitly_wait(10)
        self.find(By.XPATH, '//*[@resource-id="android:id/tabhost"]//*[@text="行情"]').click()
        self._driver.implicitly_wait(3)
        return Market(self._driver)

    def goto_my(self):
        pass
