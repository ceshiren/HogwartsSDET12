import json


def response(flow):
    if "quote.json" in flow.request.pretty_url:
        data = json.loads(flow.response.content)
        data['data']['items'][0]['quote']['name'] = "hogwarts00001"
        data['data']['items'][1]['quote']['name'] = "hogwarts00002"
        data['data']['items'][1]['quote']['current'] = 123000
        flow.response.text = json.dumps(data)
