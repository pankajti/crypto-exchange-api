import schedule
from binance_exchange_api.rest.api_caller import get_price,place_new_order_test, place_new_order
import time
import datetime as dt

from binance_exchange_api.rest.api_caller import get_account_info
from database.schema.db_model import PortfolioDetails
from database.dao.portfolio_dao import insert_record
import schedule
from binance_exchange_api.rest.api_caller import get_price
import time
import datetime as dt

#accounts = get_account_info()
#balances = [acc for acc in accounts['balances'] if float(acc['free']) > 0]
price_dict = dict()
balance_dict = dict()

def run_trades():
    symbol = 'ADABTC'
    target_price = 0.00004900
    side = 'SELL'
    quantity = 50
    price_btc = float(get_price(symbol)['price'])
    if price_btc > target_price:
        print(f"can place buy order for {symbol} for price of {price_btc}")
        #place_new_order(symbol, quantity= quantity, side=side)
    else:
        print(f" cann't place order yet for {target_price} current_price = {price_btc}")

schedule.every(30).seconds.do(run_trades)
while True:
    schedule.run_pending()
    time.sleep(1)