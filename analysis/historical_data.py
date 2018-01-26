from binance_exchange_api.rest import api_caller
import pandas as pd



all_Symbol_stats=api_caller.get_24hour_stats(None)
print(all_Symbol_stats)
