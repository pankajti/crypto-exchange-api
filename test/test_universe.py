from database.schema.db_model import UniverseTemp
from database.dao.universe_dao import insert_record


rec=UniverseTemp()
rec.base_currency='BTC'
rec.exchange='binance'
rec.quote_currency='ETH'
rec.symbol='BTCETH'
insert_record(rec)