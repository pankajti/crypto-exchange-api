import pandas as pd
import os
import datetime as dt
from config.config import COIN_MKTCAP_CONFIG

from binance_exchange_api.rest import api_caller
import coinmarketcapapi
api_key =     COIN_MKTCAP_CONFIG['api_keys'][0]['api_key']
api = coinmarketcapapi.CoinMarketCapAPI(api_key)
listings_cap_max_10000= api.cryptocurrency_listings_latest(market_cap_max=10000, limit = 5000)
listings_cap_min_10000= api.cryptocurrency_listings_latest(market_cap_min=10000, limit = 5000)


def download_market_data(root_dir, interval ='1h'):
    exchange_info = api_caller.get_exchange_info()
    all_coins = []
    coins = [a['baseAsset'] for a in exchange_info['symbols'] if
             (a['symbol'][-3:] == 'BTC') and a['status'] == 'TRADING']
    hnn = set(
        [a['symbol'] for a in listings_cap_min_10000.data if a['quote']['USD']['volume_24h'] > 200000000]).intersection(
        set(coins))
    lnn = set(
        [a['symbol'] for a in listings_cap_max_10000.data if a['quote']['USD']['volume_24h'] > 200000]).intersection(
        set(coins))
    os.makedirs(root_dir, exist_ok=True)
    all_coins.extend(hnn)
    all_coins.extend(lnn)
    for coin in all_coins:
        coin_data = []
        symbol = f'{coin}BTC'
        file_path = f'{root_dir}/{symbol}{interval}.csv'
        print(f'starting for symbol {symbol}')
        if os.path.exists(file_path):
            coin_data = pd.read_csv(file_path, index_col=0)
            print(f"reading data from {file_path}")
        if len(coin_data) == 0:
            resp = api_caller.get_kline(symbol=symbol, interval=interval)
            df = pd.DataFrame(resp)
            df = df.set_index(0)
            print(f"reading data from api")
            df = df.astype('float')
            df.columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Closetime', 'QuoteAssetVolume', 'NumberTrades',
                          'TakerByBaseAssetVolume', 'TakerByQuoteAssetVolumne', 'Ignore']
            df.to_csv(file_path, index=True)

if __name__ == '__main__':
    timenow = dt.datetime.now().strftime('%Y%m%d%H')
    print(timenow)
    root_dir =  os.path.join('./data', timenow)

    download_market_data(root_dir)
