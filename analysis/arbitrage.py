import pandas as pd
from database.schema.db_connection import engine
from bittrex_exchange_api.rest.api_caller import get_price as get_bittres_price
from binance_exchange_api.rest.api_caller import get_price_info as get_binance_price
import datetime as dt

bittrex_data=pd.read_sql("select * from universe_temp where exchange='bittrex'",engine )
binance_data=pd.read_sql("select * from universe_temp where exchange='binance'",engine )

merged=pd.merge(binance_data,bittrex_data,on=['base_currency','quote_currency'],how='inner')


def get_price_values(binance_price, bittrex_price):
    bitrex_price_val=bittrex_price['result']['Last']
    binance_price_val=float(binance_price[0]['price'])
    val_time=binance_price[0]['time']
    price_diff = binance_price_val - bitrex_price_val
    percentage_diff=(price_diff / binance_price_val) * 100
    return (binance_price_val,bitrex_price_val,val_time,price_diff,percentage_diff)


date_suf = dt.datetime.now().strftime('%Y%d%m%H%M')

with open ('/Users/pankaj/dev/git/crypto-exchange-api/result/arbitrage/result_{}.csv'.format(date_suf),'a') as f:
    header='binance_symbol', 'bittrex_symbol', 'binance_price_val', 'bitrex_price_val', 'val_time,price_diff', 'percentage_diff'
    #f.write('{},{},{},{},{},{},{},{}\n'.format(header))

    for index,record in merged.iterrows() :
        binance_symbol=record['symbol_x']
        bittrex_symbol=record['symbol_y']
        bittrex_price=get_bittres_price(bittrex_symbol)
        binance_price=get_binance_price(binance_symbol)
        price_vals=get_price_values(binance_price, bittrex_price)
        f.write('{},{},{},{},{},{},{}\n'.format(binance_symbol,bittrex_symbol,*price_vals))
        print('{},{},{},{},{},{},{}'.format(binance_symbol,bittrex_symbol,*price_vals))



