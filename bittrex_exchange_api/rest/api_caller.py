import requests
import demjson
import json

baseurl = 'https://bittrex.com'
api_call_url_format = baseurl + "{}"


def call_universe_api():
    response = requests.get(api_call_url_format.format('/api/v1.1/public/getmarkets'))
    json_format_resp=response.text.replace('true', '"true"')
    json_resp=json.loads(json_format_resp)
    return json_resp


def get_price(market):
    response = requests.get(api_call_url_format.format('/api/v1.1/public/getticker?market={}'.format(market)))
    json_resp = demjson.decode(response.text)
    return json_resp






