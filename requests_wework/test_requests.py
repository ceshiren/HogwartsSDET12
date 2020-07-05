import re

import pytest
import requests
from filelock import FileLock

from requests_wework.api.wework import WeWork


@pytest.fixture(scope="session")
def test_token():
    res = None
    # 获取 token
    while FileLock("session.lock"):
        corpid = "wwe653983e4c732493"
        corpsecret = "T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc"
        res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&"
                           f"corpsecret={corpsecret}")
    return res.json()["access_token"]


def test_get(userid, test_token):
    # 根据 user-id查询成员
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token}&userid={userid}")
    return res.json()


def test_create(userid, name, mobile, test_token):
    # 添加成员
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [1],
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token}",
                        json=data
                        )
    print(res.json())
    return res.json()


def test_update(userid, name, mobile, test_token):
    # 更新成员
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token}",
                        json=data)
    return res.json()


def test_delete(userid, test_token):
    # 删除成员
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token}&userid={userid}")
    return res.json()


def test_create_data():
    data = [("wu123fff" + str(x), "zhangsan", "138%08d" % x) for x in range(20)]
    return data


@pytest.mark.parametrize("userid, name, mobile", test_create_data())
def test_all(userid, name, mobile, test_token):
    # 可能发生创建失败
    try:
        assert "created" == test_create(userid, name, mobile, test_token)["errmsg"]
    except AssertionError as e:
        if "mobile existed" in e.__str__():
            # 如果手机号被使用了，找出使用手机号的 userid ，进行删除
            re_userid = re.findall(":(.*)", e.__str__())[0]
            if re_userid.endswith("'") or re_userid.endswith('"'):
                re_userid = re_userid[:-1]
            assert "deleted" == test_delete(re_userid, test_token)['errmsg']
            assert 60111 == test_get(re_userid, test_token)['errcode']
            assert "created" == test_create(userid, name, mobile, test_token)["errmsg"]
    # 可能发生userid不存在异常
    assert name == test_get(userid, test_token)['name']
    assert "updated" == test_update(userid, "xxxxxxx", mobile, test_token)['errmsg']
    assert "xxxxxxx" == test_get(userid, test_token)['name']
    assert "deleted" == test_delete(userid, test_token)['errmsg']
    assert 60111 == test_get(userid, test_token)['errcode']


def test_session():
    s = requests.Session()
    s.params = {
        "access_token": WeWork().get_token("T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc")
    }

    res = s.get("https://qyapi.weixin.qq.com/cgi-bin/user/get?userid=abcdef")
    print(res.json())
