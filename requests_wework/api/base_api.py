import json

import allure
import requests


class BaseApi:

    def send(self, data):
        allure.attach(str(data), attachment_type=allure.attachment_type.TEXT)
        return requests.request(**data).json()
