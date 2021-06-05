import schedule
from binance_exchange_api.rest.api_caller import get_price,place_new_order_test
import time
import datetime as dt

from binance_exchange_api.rest.api_caller import get_account_info
from database.schema.db_model import PortfolioDetails
from database.dao.portfolio_dao import insert_record
import schedule
from binance_exchange_api.rest.api_caller import get_price
import time
import datetime as dt

accounts = get_account_info()
balances = [acc for acc in accounts['balances'] if float(acc['free']) > 0]
price_dict = dict()
balance_dict = dict()

def init_price():
    base_currency = 'BTC'
    for balance in balances:
        asset = balance['asset']
        if asset != base_currency:
            symbol = f'{asset}{base_currency}'
            price = float(get_price(symbol)['price'])
            price_dict[symbol] = price
            balance_dict[asset] = float(balance['free'])
    print("initialization done ")

def run_trades():
    price_btc = float(get_price('BTCUSDT')['price'])
    profits = 0
    total_base_currency= 0
    base_currency = 'BTC'
    for balance in balances :
        asset = balance['asset']
        if asset!= base_currency:

            symbol = f'{asset}{base_currency}'
            free_bal = balance_dict[asset]

            price = float(get_price(symbol)['price'])
            if price > price_dict[symbol]*1.05:
                profit = free_bal*price
                print(f"can place buy order for {symbol} for profit of {profit}")
                price_dict[symbol] = price
                #place_new_order_test(symbol)
                profits = profits +profit
                balance_dict[symbol] = 0

            if price < price_dict[symbol]*.95:
                profit = free_bal*price
                print(f"can place sell order for {symbol} for loss of {profit}")
                price_dict[symbol] = price
                #place_new_order_test(symbol)
                profits = profits - profit
                balance_dict[symbol] = free_bal
    print(f"total profit {profits}")


init_price()
schedule.every(20).seconds.do(run_trades)
while True:
    schedule.run_pending()
    time.sleep(1)