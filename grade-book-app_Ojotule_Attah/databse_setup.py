from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course

engine = create_engine('sqlite:///gradebook.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

