from binance_exchange_api.rest import api_caller
import pandas as pd


account_balances=api_caller.get_account_info()

account_data=pd.DataFrame(account_balances['balances'], dtype=float)

account_data=account_data[account_data['free']>0]

for asset in account_data['asset']:
    trades=api_caller.get_all_trades(asset+'BTC')
    print(trades)