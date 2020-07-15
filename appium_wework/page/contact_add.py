from appium.webdriver.common.mobileby import MobileBy

from appium_wework.page.base_page import BasePage


class ContactAdd(BasePage):

    def input_name(self, username):
        nameelement = self.find(MobileBy.XPATH,
                                "//*[@text='姓名　']/..//*[@class='android.widget.EditText']")
        nameelement.send_keys(username)

        return self

    def set_gender(self, gender):
        self.find(MobileBy.XPATH,
                  "//*[@text='性别']/..//*[contains(@class, 'TextView') and @text='男']").click()
        if gender == '女':
            self.find(MobileBy.XPATH, "//*[@text='女']").click()
        else:
            self.find(MobileBy.XPATH, "//*[@text='男']").click()

        return self

    def input_phonenum(self, phonenum):
        phonenum_element = self.find(MobileBy.XPATH,
                                     "//*[@text='手机　']/..//*[contains(@class, 'EditText')]")
        phonenum_element.send_keys(phonenum)

        return self

    def click_save(self):
        from appium_wework.page.member_invit import MemberInvite
        self.find(MobileBy.ID, "com.tencent.wework:id/gur").click()

        return MemberInvite(self._driver)
