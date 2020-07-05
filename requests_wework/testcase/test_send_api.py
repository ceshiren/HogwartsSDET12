from requests_wework.action.api_action import api_action
from requests_wework.core.content import Content


def test_send_api():
    content = Content("./work.yaml")
    expression = api_action(content)
    res = expression.run_fun('get')
    print(res)