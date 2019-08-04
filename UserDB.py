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
	password_hash = Column(String)
	tickets = Column(String)
    points=Column(Integer)
    image=Column(String)


	def hash_password(self, password):
        self.password_hash = pwd_security.encrypt(password)
    def verify_password(self, password):
        return pwd_security.verify(password, self.password_hash)

	def __repr__(self):
		return ("Username: {}\n").format(self.name)

