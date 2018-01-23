import requests
import json

baseurl='https://api.binance.com'

api_call_url_format=baseurl+"{}"

response = requests.get(api_call_url_format.format('/api/v1/exchangeInfo'))
json_resp=json.loads(response.text)

print(json_resp)


