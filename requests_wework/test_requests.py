import requests


def test_token():
    # 获取 token
    corpid = "wwe653983e4c732493"
    corpsecret = "T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc"
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    return res.json()["access_token"]


def test_get():
    # 根据 user-id查询成员
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token()}&userid=zhangsan")
    print(res.json())


def test_create():
    # 添加成员
    data = {
        "userid": "zhangsan",
        "name": "张三",
        "mobile": "13800000000",
        "department": [1],
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token()}",
                        json=data
                        )
    print(res.json())


def test_update():
    # 更新成员
    data = {
        "userid": "zhangsan",
        "name": "小红",
        "mobile": "13811110000",
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token()}",
                        json=data)
    print(res.json())


def test_delete():
    # 删除成员
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token()}&userid=zhangsan")
    print(res.json())
