#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    # Database connection
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects
    results = session.query(City, State).join(State).order_by(City.id).all()

    # Print results
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")
