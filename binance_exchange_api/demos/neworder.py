import requests
import json
import time
import math
import hmac
import hashlib





def place_new_order():
    api_key = ''
    secret = ''

    baseurl = 'https://api.binance.com'
    api_call_url_format = baseurl + "{}"

    headers = {'X-MBX-APIKEY': api_key}
    payload = {'symbol': 'ETHBTC', 'side': 'BUY', 'type': 'MARKET', 'quantity': '12',
               'timestamp': math.floor(time.time() * 1000), 'recvWindow': 500000000}

    query_str = ''
    for key, val in payload.items():
        query_str += key + "=" + str(val) + "&"
    m = hmac.new(secret.encode('utf-8'), query_str[:len(query_str)-1].encode('utf-8'), hashlib.sha256)
    signature= m.hexdigest()
    payload['signature']=signature
    response = requests.post(api_call_url_format.format('/api/v3/order/test'),headers=headers,data=payload)
    json_resp=json.loads(response.text)
    return json_resp

place_new_order()