import requests
import json

response=requests.get('https://bittrex.com/api/v1.1/public/getmarkets')

json_resp=json.dumps(response.text)

print(json_resp)