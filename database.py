from  UserDB import *
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker

engine = create_engine('sqlite:///students.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



def check_username(username):

    return session.query(User).filter_by(name=username).first()