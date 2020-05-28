from appium_wework.page.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_addcontact(self):
        invitpage = self.main.goto_addresslist().add_member(). \
            addmember_by_manul().input_name().set_gender() \
            .input_phonenum().click_save()

        # assert '成功' in invitpage.get_toast()
