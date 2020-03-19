from binance_exchange_api.rest import api_caller
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

trades_24hour=api_caller.get_24hour_stats()

trades_data=pd.DataFrame(trades_24hour,dtype=float)
trades_data.plot(x='lastPrice',y='volume')



plt.plot(trades_data['lastPrice'],trades_data['volume'])


print(trades_data)



