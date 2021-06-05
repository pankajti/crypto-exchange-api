from binance_exchange_api.rest.api_caller import get_account_info

accounts = get_account_info()
balances = [acc for acc in accounts['balances'] if float(acc['free']) > 0]

#alphas = get_alphas()

""" 
steps : 
get_all alpha signals 

get all existing open positions 
    allocate fund for each symbol to buy 
    calculate buy quantity based on existing price
    execute the trade

close positions with sell signals 
    get number of positions
    execute trade with sell quantity

open positions with buy signals 

"""
