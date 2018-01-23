import requests

baseurl='https://api.binance.com'

api_call_url_format=baseurl+"{}"


response = requests.get(api_call_url_format.format('/api/v1/ping'))

print(response)


response = requests.get(api_call_url_format.format('/api/v1/ping'))
