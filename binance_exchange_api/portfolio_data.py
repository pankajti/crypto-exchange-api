from binance_exchange_api.rest.api_caller import get_account_info
from database.schema.db_model import PortfolioDetails
from database.dao.portfolio_dao import insert_record
import schedule
from binance_exchange_api.rest.api_caller import get_price
import time
import datetime as dt

def main():
    price_eth = float(get_price('ETHUSDT')['price'])
    price_btc = float(get_price('BTCUSDT')['price'])
    accounts = get_account_info()
    balances  = [acc for acc in accounts['balances'] if float(acc['free'])>0]
    total_base_currency= 0
    base_currency = 'BTC'
    for balance in balances :
        asset = balance['asset']
        free_bal =float(balance['free'])
        if asset== base_currency:
            total_base_currency = total_base_currency + free_bal
        else:
            price = float(get_price(f'{asset}{base_currency}')['price'])
            total_base_currency = total_base_currency + free_bal*price
    print(f"total {base_currency} : {total_base_currency} , Total USD : {total_base_currency*price_btc}")

if __name__ == '__main__':
    main()
