from bittrex_exchange_api.rest.api_caller import call_universe_api
from database.schema.db_model import UniverseTemp
from database.dao.universe_dao import insert_record


def create_universe_records(response):
    universe_records =list()
    all_symbols=response['result']
    for symbol in all_symbols:
        univ_rec=UniverseTemp()
        univ_rec.symbol=symbol['MarketName']
        univ_rec.quote_currency=symbol['BaseCurrency']
        univ_rec.base_currency=symbol['MarketCurrency']
        univ_rec.exchange='bittrex'
        insert_record(univ_rec)
        print('inserted symbol : {}'.format(symbol))
    return universe_records


response=call_universe_api()

create_universe_records(response)