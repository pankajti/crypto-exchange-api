from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer,DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:postgres@localhost:5432/crypto')

connection = engine.connect()

Base=declarative_base()

class UniverseTemp(Base):
    __tablename__='universe_temp'
    id=Column(Integer, primary_key=True)
    base_currency=Column(String)
    quote_currency=Column(String)
    symbol=Column(String)
    exchange=Column(String)


def create_schema():
    result=Base.metadata.create_all(engine)
    print("Schema created successfully")

create_schema()





