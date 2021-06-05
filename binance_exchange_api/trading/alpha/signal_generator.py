from binance_exchange_api.trading.alpha.signals import *
from binance_exchange_api.trading.data_downloader import *
import datetime as dt
def macd_signal_generator(df):
    macd, macd_sig, _ = MACD(df.Close.values)
    up_move = cross_over(macd, macd_sig)
    down_move = False
    if not up_move:
        down_move = cross_over(macd_sig, macd)
    return up_move , down_move

def bb_signal_generator(df):
    close = df.Close.values
    upperband, middleband, lowerband = BBAND(close)
    up_move = cross_over(close, upperband)
    down_move = cross_over(lowerband, close)
    return up_move , down_move

def rsi_signal_generator(df):
    rsi = RSI(df.Close.values)[-1]
    up_move= False
    down_move = False
    if rsi < 30:
        up_move = True
    if rsi > 70:
        down_move = True
    return up_move , down_move

def sma_cross_signal_generator(df):
    sma_7 = SMA(df.Close.values, 7)
    sma_25 = SMA(df.Close.values, 25)
    up_move = cross_over(sma_7, sma_25)
    down_move = cross_over(sma_25, sma_7)
    return up_move , down_move
signals_generator_dict  = {'MACD': macd_signal_generator, 'BB':bb_signal_generator, 'RSI':rsi_signal_generator,
                           'SMA_CROSS':sma_cross_signal_generator}


def generate_signals ():
    timenow = dt.datetime.now().strftime('%Y%m%d%H')
    print(timenow)
    root_dir =  os.path.join('./data/market', timenow)
    download_market_data(root_dir)
    indicators =[]
    files = os.listdir(root_dir)
    for file  in files :
        symbol = file[:-6]
        file_path = os.path.join(root_dir, file)
        df = pd.read_csv(file_path)
        for signal , generator in signals_generator_dict.items():
            up_move , down_move = generator(df)
            indicator = {'signal': signal, 'symbol':symbol, 'direction' : (int(up_move)-int(down_move))}
            indicators.append(indicator)
    indicators_df = pd.DataFrame(indicators)
    alpha_signals = indicators_df.pivot(index='signal', columns='symbol')
    movers =alpha_signals.T[alpha_signals.any() != 0].reset_index().drop(['level_0'], axis=1)
    movers.to_csv(f'{root_dir}/../{timenow}_alpha_signals.csv')

    alpha_signals=alpha_signals.T[alpha_signals.T.BB != 0]
    combo_sig = alpha_signals.sum(axis=1).reset_index()
    buy = combo_sig[combo_sig[0]>0]
    buy.to_csv(f'{root_dir}/../{timenow}_buy.csv')
    sell = combo_sig[combo_sig[0]<0]
    sell.to_csv(f'{root_dir}/../{timenow}_sell.csv')

    print(buy)
generate_signals()
import schedule
import time
schedule.every(3600).seconds.do(generate_signals)
while True:
    schedule.run_pending()
    time.sleep(1)