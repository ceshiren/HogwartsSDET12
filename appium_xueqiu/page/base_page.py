import logging

from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from appium_xueqiu.page.wrapper import handle_black


class BasePage:
    # 弹框 处理的定位列表

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def finds(self, locator, value: str = None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @handle_black
    def find(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    def find_and_get_text(self, locator, value: str = None):
        element: WebElement
        try:
            element_text = self._driver.find_element(*locator).text if isinstance(locator,
                                                                                  tuple) else self._driver.find_element(
                locator, value).text
            # if isinstance(locator, tuple):
            #     element =  self._driver.find_element(*locator)
            # else:
            #     element = self._driver.find_element(locator,value)
            # 找到之前 _error_num 归0
            self._error_num = 0
            # 隐式等待回复原来的等待，
            self._driver.implicitly_wait(10)
            return element_text
        except Exception as e:
            # 出现异常， 将隐式等待设置小一点，快速的处理弹框
            self._driver.implicitly_wait(1)
            # 判断异常处理次数
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1
            # 处理黑名单里面的弹框
            for ele in self._black_list:
                elelist = self._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # 处理完弹框，再将去查找目标元素
                    return self.find_and_get_text(locator, value)

            raise e
