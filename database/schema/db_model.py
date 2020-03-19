from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer,DateTime,Numeric
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:postgres@localhost:5432/crypto')


Base=declarative_base()

class UniverseTemp(Base):
    __tablename__='universe_temp'
    id=Column(Integer, primary_key=True)
    base_currency=Column(String)
    quote_currency=Column(String)
    symbol=Column(String)
    exchange=Column(String)


class PortfolioDetails(Base):
    __tablename__='portfolio_details'
    id=Column(Integer, primary_key=True)
    portfolio_id=Column(Integer)
    symbol=Column(String)
    exchange=Column(String)
    quantity=Column(Numeric)
    buy_price=Column(Numeric)
    ccy=Column(String)

class Portfolios(Base):
    __tablename__='portfolios'

    id = Column(Integer, primary_key=True)
    name = Column(String)




def create_schema():
    result=Base.metadata.create_all(engine)
    print("Schema created successfully")

create_schema()





