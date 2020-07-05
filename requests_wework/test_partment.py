import requests


def test_token():
    res = None
    # 获取 token
    corpid = "wwe653983e4c732493"
    corpsecret = "T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc"
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&"
                       f"corpsecret={corpsecret}")
    return res.json()["access_token"]


def test_create():
    data = {
        "name": "广州研发中心",
        "parentid": 1
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_token()}",
                        json=data)
    print(res.json())


def test_update():
    data = {
        "id": 2,
        "name": "广州研发中心123456"
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_token()}",
                        json=data)
    print(res.json())


def test_delete():
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_token()}&id=2")
    print(res.json())


def test_get():
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_token()}")
    print(res.json())
