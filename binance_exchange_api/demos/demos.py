import requests
import demjson
baseurl='https://api.binance.com'

api_call_url_format=baseurl+"{}"
response = requests.get(api_call_url_format.format('/api/v1/trades?symbol=ETHBTC&limit=1'))
json_text=response.text
json_resp=demjson.decode(json_text)
print(json_resp)

response = requests.get(api_call_url_format.format('/api/v1/ping'))
