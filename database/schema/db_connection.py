from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import  psycopg2

engine = create_engine('postgresql://postgres:postgres@localhost:5432/crypto')


def get_session():
    Session = sessionmaker(bind=engine)
    return   Session()

