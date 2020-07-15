import pytest
import yaml

from appium_wework.page.app import App

with open('../datas/contact.yml') as f:
    addlists = yaml.safe_load(f)['add']


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    @pytest.mark.parametrize('username, gender,phonenum', addlists)
    def test_addcontact(self, username, gender, phonenum):
        # invitpage = self.main.goto_addresslist().add_member(). \
        #     addmember_by_manul().input_name(username).set_gender(gender) \
        #     .input_phonenum(phonenum).click_save()
        print(addlists)

        # assert '成功' in invitpage.get_toast()

    def teardown(self):
        self.app.stop()
