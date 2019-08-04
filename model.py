 

class Events(Base):

	__tablename__ = 'events'
	event_id = Column(Integer, primary_key = True)
	event = Column(String)        #radio (movie, coffee, conversion, park meeting, volenteer, selling)
	user_id = Column(PickleType)  #list of users going to this event
	location = Column(String)
	organizer = Column(Integer)    #User id of the creator
	description = Column(String)   #description of the event
	maximum = Column(Integer)      #Maximum of participant check list of users
	time = Column(String)

class Tickets:

	__tablename__ = 'tickets'

