from model import Base, Event

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///students.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_event(name, icon, des, time, loc, maxi):
	
	eve = Event(
		event=name,
		image = icon,
		description = des,
		time = time,
		maximum = maxi,
		location = loc
		)
	session.add(eve)
	session.commit()

def add_points(user_id):
	user = session.query(
       User).filter_by(
       user_id=user_id).first()
	user.points += 10




