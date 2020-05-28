from appium.webdriver.common.mobileby import MobileBy

from appium_wework.page.base_page import BasePage


class ContactAdd(BasePage):

    def input_name(self):
        nameelement = self.find(MobileBy.XPATH,
                                "//*[@text='姓名　']/..//*[@class='android.widget.EditText']")
        nameelement.send_keys("霍格name1")

        return self

    def set_gender(self):
        self.find(MobileBy.XPATH,
                  "//*[@text='性别']/..//*[contains(@class, 'TextView') and @text='男']").click()
        self.find(MobileBy.XPATH, "//*[@text='女']").click()

        return self

    def input_phonenum(self):
        phonenum_element = self.find(MobileBy.XPATH,
                                     "//*[@text='手机　']/..//*[contains(@class, 'EditText')]")
        phonenum_element.send_keys("18712345678")

        return self

    def click_save(self):
        from appium_wework.page.member_invit import MemberInvite
        self.find(MobileBy.ID, "com.tencent.wework:id/gur").click()

        return MemberInvite(self._driver)
