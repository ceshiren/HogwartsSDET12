import requests


class BaseApi:

    def send(self, data):
        return requests.request(**data).json()
