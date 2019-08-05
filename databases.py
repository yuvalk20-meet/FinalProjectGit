from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///students.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_event(name, icon, des, time, loc, maxi, org):
	
	eve = Event(
		event=name,
		image = icon,
		description = des,
		time = time,
		maximum = maxi,
		location = loc,
		organizer = org
		)
	session.add(eve)
	session.commit()


def add_points(user_id):
	user = session.query(
       User).filter_by(
       user_id=user_id).first()
	user.points += 10

def query_all():
	return session.query(Event).all()

def check_username(username):

    return session.query(User).filter_by(name=username).first()

def addUser(username,password,age,number,gender,niborhood):

    user=User(name=username,phone_number=number,gender=gender,neiborhood=niborhood, points = 0)
    print(user)
    user.hash_password(password)
 
    session.add(user)
    session.commit()
