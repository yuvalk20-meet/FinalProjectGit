from sqlalchemy import Column, Integer, String, Boolean, PickleType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	
	__tablename__ = 'user'
	user_id = Column(Integer, primary_key=True)
	name = Column(String)
	age = Column(Integer)
	phone_number = Column(Integer)
	gender = Column(String)   #radio
	neiborhood = Column(String)   #radio
	tickets = Column(String)
	points = Column(Integer)
	password_hash = Column(String)

	def __repr__(self):
		return ("Username: {}\n").format(self.name)

	
    
	def hash_password(self, password):
		self.password_hash = pwd_security.encrypt(password)
	def verify_password(self, password):
		return pwd_security.verify(password, self.password_hash)

class Event(Base):

	__tablename__ = 'events'
	event_id = Column(Integer, primary_key = True)
	event = Column(String)        #radio (movie, coffee, conversion, park meeting, volenteer, selling)
	user_id = Column(PickleType)  #list of users going to this event
	location = Column(String)
	organizer = Column(Integer)    #User id of the creator
	description = Column(String)   #description of the event
	maximum = Column(Integer)      #Maximum of participant check list of users
	time = Column(String)
	image = Column(String)  #Url of icon

class Tickets:

	__tablename__ = 'tickets'

