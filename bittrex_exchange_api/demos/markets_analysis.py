import requests
import demjson

#response=requests.get('https://bittrex.com/api/v1.1/public/getmarkets')

response=requests.get('https://bittrex.com/api/v1.1/public/getticker?market=BTC-LTC')
json_resp=demjson.decode(response.text)

print(json_resp)