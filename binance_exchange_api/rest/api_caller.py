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

def get_24hour_stats(symbol=None):
    api= '/api/v1/ticker/24hr' if symbol==None else '/api/v1/ticker/24hr?symbol={}'.format(symbol)
    response=requests.get(api_call_url_format.format(api))
    if response.status_code=='429':
        print('Warning ::: stop requesting more data')
    return json.loads(response.text)

def get_price(symbol=None):
    api='/api/v3/ticker/price' if symbol==None else '/api/v3/ticker/price?symbol={}'.format(symbol)
    response=requests.get(api_call_url_format.format(api))
    return json.loads(response.text)




