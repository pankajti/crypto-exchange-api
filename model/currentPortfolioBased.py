from binance_exchange_api.rest import api_caller
import pandas as pd
import matplotlib
import sklearn

def getCurrentPositions():
    account_info=api_caller.get_account_info()
    account_data=pd.DataFrame(account_info['balances'],dtype=float)
    account_data=account_data[account_data.free.astype(float)>0.0]

    account_data.index=range(len(account_data))
    btc_price=float(api_caller.get_price('BTCUSDT')['price'])
    eth_price=float(api_caller.get_price('ETHUSDT')['price'])
    all_pos=[]

    for index, row  in account_data.iterrows():
        asset=row['asset']
        print(asset)

        for base_currency in ['BTC','ETH']:
            if asset==base_currency:
                continue
            symbol=asset+base_currency
            btctrades=api_caller.get_all_trades(symbol)
            if len(btctrades)<1 or ('code' in btctrades and  btctrades['code']==-1121):
                continue

            pos_data={}
            btctradesdata=pd.DataFrame(btctrades,dtype=float)
            total_buy_value=0.0
            total_quantity=0.0
            current_price=float(api_caller.get_price(symbol)['price'])
            for idx, row in btctradesdata.iterrows():
                mult= 1 if row['isBuyer']==True else -1
                total_buy_value+=float(row['price'])*float(row['qty'])*mult
                total_quantity+=float(row['qty'])*mult

            base_currency_price=(btc_price if base_currency=='BTC' else eth_price)

            avg_price=total_buy_value/total_quantity
            pos_data['base_currency']=base_currency
            pos_data['asset']=asset
            pos_data['avg_price']=avg_price
            pos_data['qty']=total_quantity
            pos_data['current_price']=current_price
            pos_data['CURR_USD_PRICE']=total_quantity*current_price*base_currency_price
            pos_data['BUY_USD_PRICE']=total_quantity*avg_price*base_currency_price
            all_pos.append(pos_data)


    return all_pos 




if __name__=='__main__':
    positions =getCurrentPositions()
    print(positions)
