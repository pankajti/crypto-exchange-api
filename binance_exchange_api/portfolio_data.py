from binance_exchange_api.rest.api_caller import call_universe_api
from database.schema.db_model import PortfolioDetails
from database.dao.portfolio_dao import insert_record


import schedule
from binance_exchange_api.rest.api_caller import get_price
import time
import datetime as dt
binance_symbol_btc={'TNBBTC':332.66700000,'ADABTC':65.93400000,'XRPBTC':21.97800000}
binance_symbol_eth={'IOSTETH':251.748,'ICXETH':3.38661000}
price_eth=float(get_price('ETHUSDT')['price'])
price_btc=float(get_price('BTCUSDT')['price'])



def calculate_total_coins(wallet):
    coins=0
    for symbol, qty in wallet.items():
        pd = PortfolioDetails()
        price = float(get_price(symbol)['price'])
        pd.symbol=symbol
        pd.exchange='binance'
        pd.quantity=qty
        pd.portfolio_id=1
        pd.ccy='USD'
        if symbol[-3:]=='BTC':
            pd.buy_price = price*price_btc
        else:
            pd.buy_price = price*price_eth
        print(pd)
        #insert_record(pd)
        coins=coins+qty
    return coins

def calculate_portfolio_value():
    eth=calculate_total_coins(binance_symbol_eth)
    btc=calculate_total_coins(binance_symbol_btc)
    total_val=price_btc*btc+price_eth*eth
    print(dt.datetime.now().strftime('%Y%d%m%H%M%S')+","+ str(total_val))

calculate_portfolio_value()
