#!/usr/bin/python3
"""
A script that updates the name of a State object in a database.
It takes the user, password, and database name as command line arguments.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
from urllib.parse import quote_plus

if __name__ == "__main__":
    """
    Connect to database and update state name
    """
    user = sys.argv[1]
    # URL encode the password
    password = quote_plus(sys.argv[2])
    db = sys.argv[3]

    db_url = f'mysql+mysqldb://{user}:{password}@localhost/{db}'
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the state with id 2
    state = session.query(State).filter(State.id == 2).first()
    
    # Check if state exists
    if state:
        # Update the name of the state
        state.name = 'New Mexico'
        # Commit the changes
        session.commit()
    
    session.close()
