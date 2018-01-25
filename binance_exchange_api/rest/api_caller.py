import requests
import json

baseurl = 'https://api.binance.com'
api_call_url_format = baseurl + "{}"


def call_universe_api():
    response = requests.get(api_call_url_format.format('/api/v1/exchangeInfo'))
    json_resp=json.loads(response.text)
    return json_resp

def get_price_info(symbol):
    response = requests.get(api_call_url_format.format('/api/v1/trades?symbol={}&limit=1'.format(symbol)))
    json_resp=json.loads(response.text)
    return(json_resp)






