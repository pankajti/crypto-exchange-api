import pandas as pd
import os
from binance_exchange_api.rest import api_caller
import datetime as dt
coin_data = []
exchange_info = api_caller.get_exchange_info()
from config.config import COIN_MKTCAP_CONFIG

coins = [ a['baseAsset'] for a in exchange_info['symbols'] if (a['symbol'][-3:]=='BTC') and a['status']=='TRADING']

import coinmarketcapapi
api_key =     COIN_MKTCAP_CONFIG['api_keys'][0]['api_key']


api = coinmarketcapapi.CoinMarketCapAPI(api_key)
listings_cap_max_10000= api.cryptocurrency_listings_latest(market_cap_max=10000, limit = 5000)
listings_cap_min_10000= api.cryptocurrency_listings_latest(market_cap_min=10000, limit = 5000)
hnn = set([a['symbol'] for a in listings_cap_min_10000.data if a['quote']['USD']['volume_24h']>200000000 ]).intersection(set(coins))
lnn = set([a['symbol'] for a in listings_cap_max_10000.data if a['quote']['USD']['volume_24h']>200000 ]).intersection(set(coins))
print("A")
