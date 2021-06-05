import unittest
from binance_exchange_api.rest import api_caller
import nose
class ApiCallerTestCase(unittest.TestCase):
    def test_call_univers(self):
        univ = api_caller.call_universe_api()
        num_symbols = len(univ['symbols'])
        self.assertTrue(num_symbols>0)

    def test_my_trades(self):
        trades = api_caller.get_all_trades()
        print(trades)


if __name__ == '__main__':
    unittest.main()
