from binance_exchange_api.rest import api_caller


class ApiCallerTestCase():

    def __init__(self, symbol):
        self.symbol = symbol

    def test_call_univers(self):
        univ = api_caller.call_universe_api()
        print(univ)

    def test_price(self):
        price = api_caller.get_price(self.symbol)
        print(price)

    def test_neworder_test(self):
        resp = api_caller.place_new_order_test(self.symbol, 10)
        print(resp)

    def test_neworder(self):
        resp = api_caller.place_new_order(self.symbol, 50, 'BUY')
        print(resp)


    def test_get_kline(self):
        resp = api_caller.get_kline(symbol=self.symbol)

        print(resp)


if __name__ == '__main__':
    symbol = 'ADABTC'
    t = ApiCallerTestCase(symbol)
    #t.test_price()
    t.test_neworder()

    #t.test_get_kline()
    #t.test_call_univers()
