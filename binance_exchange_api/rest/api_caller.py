import requests
import json

baseurl = 'https://api.binance.com'


def call_universe_api():
    api_call_url_format=baseurl+"{}"
    response = requests.get(api_call_url_format.format('/api/v1/exchangeInfo'))
    json_resp=json.loads(response.text)
    return json_resp






