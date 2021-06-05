import requests
import json
from config.config import BINANCE_CONFIG
import math
import time
import hmac
import hashlib


baseurl = 'https://api.binance.com'
api_call_url_format = baseurl + "{}"

def get_exchange_info():
    response = requests.get(api_call_url_format.format('/api/v1/exchangeInfo'))
    json_resp=json.loads(response.text)
    return json_resp

def get_price_info(symbol):
    response = requests.get(api_call_url_format.format('/api/v1/trades?symbol={}&limit=1'.format(symbol)))
    json_resp=json.loads(response.text)
    return(json_resp)

def get_24hour_stats(symbol=None):
    api= '/api/v1/ticker/24hr' if symbol==None else \
        '/api/v1/ticker/24hr?symbol={}'.format(symbol)
    response=requests.get(api_call_url_format.format(api))
    if response.status_code=='429':
        print('Warning ::: stop requesting more data')
    return json.loads(response.text)

def get_price(symbol=None):
    api='/api/v3/ticker/price' if symbol==None else '/api/v3/ticker/price?symbol={}'.format(symbol)
    response=requests.get(api_call_url_format.format(api))
    return json.loads(response.text)


def get_account_info():
    payload = { 'timestamp': math.floor(time.time() * 1000), 'recvWindow': 50000}
    headers = apply_credentials(payload)
    response = requests.get(api_call_url_format.format('/api/v3/account'), headers=headers, params=payload)
    json_resp = json.loads(response.text)
    return json_resp

def place_new_order_test(symbol, quantity , side ='BUY'):
    payload = {'symbol': symbol, 'side': side, 'type': 'MARKET',
               'quantity': quantity,'timestamp': math.floor(time.time() * 1000), 'recvWindow': 50000}
    headers = apply_credentials(payload)
    response = requests.post(api_call_url_format.format('/api/v3/order/test'),headers=headers, data=payload)
    json_resp=json.loads(response.text)
    return json_resp


def place_new_order(symbol, quantity, side ='BUY' ):
    payload = {'symbol': symbol, 'side': side, 'type': 'MARKET', 'quantity': quantity,
               'timestamp': math.floor(time.time() * 1000), 'recvWindow': 50000}
    headers = apply_credentials(payload)
    response = requests.post(api_call_url_format.format('/api/v3/order'),headers=headers, data=payload)
    json_resp=json.loads(response.text)
    return json_resp


def get_kline( symbol = 'ADABTC', interval ='1m', limit = 1000):
    payload = {'timestamp': math.floor(time.time() * 1000),'recvWindow': 50000}
    headers = apply_credentials(payload)
    params = {'symbol': symbol,"interval": interval, 'limit' :limit }
    response = requests.get(api_call_url_format.format('/api/v3/klines'),headers=headers , params = params)
    json_resp=json.loads(response.text)
    return json_resp



def apply_credentials(payload):
    api_key = BINANCE_CONFIG['api_keys'][0]['api_key']
    secret = BINANCE_CONFIG['api_keys'][0]['api_secret']
    headers = {'X-MBX-APIKEY': api_key}
    query_str = ''
    for key, val in payload.items():
        query_str += key + "=" + str(val) + "&"
    m = hmac.new(secret.encode('utf-8'), query_str[:len(query_str) - 1].encode('utf-8'), hashlib.sha256)
    signature = m.hexdigest()
    payload['signature'] = signature
    return headers


def get_all_trades(symbol):
    payload = {'symbol':symbol, 'timestamp': math.floor(time.time() * 1000),
               'recvWindow': 50000}
    headers = apply_credentials(payload)
    response = requests.get(api_call_url_format.format('/api/v3/myTrades'), headers=headers, params=payload)
    json_resp = json.loads(response.text)
    return json_resp
