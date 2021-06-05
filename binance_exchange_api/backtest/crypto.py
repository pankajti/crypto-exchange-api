import pandas as pd
import os
from backtesting import Backtest
from binance_exchange_api.backtest.strategies.sma_cross_2 import SmaCross
from binance_exchange_api.backtest.strategies.macd_cros import MACDCross
from binance_exchange_api.rest import api_caller
import datetime as dt

if __name__ == '__main__':
    coin_data = []
    exchange_info = api_caller.get_exchange_info()
    symbols = [(a['symbol'], a['baseAsset']) for a in exchange_info['symbols'] if a['status'] == 'TRADING']
    results = list()
    strategy = MACDCross
    strategy_name ='MACDCross'
    #timenow = dt.datetime.now().strftime('%Y%m%d%H%M')
    timenow = '202106040823'
    interval = '1m'
    root_dir = os.path.join('./data', interval, timenow)
    os.makedirs(root_dir, exist_ok=True)
    print(f"data directory : {root_dir}")
    total_symbols = len(symbols)
    print(f"total {total_symbols} symbols to backtest")
    for idx, symbol_t in enumerate(symbols):
        coin_data = []
        symbol = symbol_t[0]
        # symbol = f'{coin}BTC'
        file_path = f'{root_dir}/{symbol}{interval}.csv'
        print(f'starting for symbol {symbol}  {idx} of {total_symbols}')
        if os.path.exists(file_path):
            coin_data = pd.read_csv(file_path, index_col=0)
            print(f"reading data from {file_path}")
        if len(coin_data) == 0:
            resp = api_caller.get_kline(symbol=symbol, interval=interval, limit=1000)
            df = pd.DataFrame(resp)
            df = df.set_index(0)
            print(f"reading data from api")
            coin_data = df.loc[:, 0:5]
            coin_data = coin_data.astype('float')
            coin_data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
            coin_data.to_csv(file_path, index=True)
            print(f"stored data at {file_path}")
        coin_data = coin_data.set_index(coin_data.index.map(lambda x: dt.datetime.fromtimestamp(x / 1000)))
        bt = Backtest(coin_data, strategy=strategy, cash=0.1, commission=.001)
        result = bt.optimize(n1=range(5, 30, 5),
                             n2=range(10, 70, 5),
                             symbol=symbol,
                             maximize='Equity Final [$]',
                             constraint=lambda param: param.n1 < param.n2
                             )

        res_dict = {l[0]: l[1] for l in list(result.items()) if l[0][0] != '_'}
        res_dict['symbol'] = symbol
        res_dict['baseAsset'] = symbol_t[1]
        res_dict['asset'] = symbol[len(symbol):]
        res_dict['strategy'] = str(result._strategy)

        results.append(res_dict)
        # bt.plot()
        print(result['_strategy'])
    pd.DataFrame(results).to_csv(f"bt_result{interval}_{strategy_name}.csv")

    print("backtesting over ")

