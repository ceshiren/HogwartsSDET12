from requests_wework.api.address import Address


class TestAddress:

    def setup(self):
        self.address = Address()

    def test_create(self):
        print(self.address.create("zhangsan2222", "wangwu", "13899999999"))

    def test_update(self):
        print(self.address.update("zhangsan2222", "wangwufffff", "13899999999"))

    def test_delete(self):
        print(self.address.delete("zhangsan2222"))
