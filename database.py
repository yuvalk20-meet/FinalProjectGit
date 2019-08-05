from  UserDB import *
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker

engine = create_engine('sqlite:///students.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



def check_username(username):

    return session.query(User).filter_by(name=username).first()

def addUser(username,password,age,number,gender,niborhood):

    user=User(name=username,password_hash=password,phone_number=number,gender=gender,neiborhood=niborhood)
    user.password_hash(password)
 
    session.add(user)
    session.commit()