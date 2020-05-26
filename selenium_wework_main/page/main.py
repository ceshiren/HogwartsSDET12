from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework_main.page.add_member import AddMember
from selenium_wework_main.page.base_page import BasePage


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def goto_add_member(self):
        # click add member
        # self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        self.find(By.ID, 'menu_contacts').click()
        def wait_add_member(x):
            elements_len = len(self.finds(By.CSS_SELECTOR, '#username'))
            if elements_len <= 0:
                self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
            return elements_len > 0
        #self.waif_for_click((By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)'))
        self.wait_for_elem(wait_add_member)
        return AddMember(self._driver)
