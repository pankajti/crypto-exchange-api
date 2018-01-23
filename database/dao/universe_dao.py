from database.schema.db_connection import get_session

session=get_session()

def insert_record(rec):
    session.add(rec)
    session.commit()
    session.flush()
    session.close()
