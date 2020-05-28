from appium.webdriver.common.mobileby import MobileBy

from appium_wework.page.base_page import BasePage


class MemberInvite(BasePage):

    def addmember_by_manul(self):
        from appium_wework.page.contact_add import ContactAdd
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        return ContactAdd(self._driver)

    def get_toast(self):
        return self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        # return "toast"
