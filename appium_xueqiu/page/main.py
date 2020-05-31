import yaml
from selenium.webdriver.common.by import By

from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.set_implicitly(10)
        self.steps("../page/main.yaml")
        self.set_implicitly(3)
        return Market(self._driver)
