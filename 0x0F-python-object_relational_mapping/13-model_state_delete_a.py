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

    # Fetch all state containing the letter a
    states = session.query(State).filter(State.name.contains('a'))

    #loop to delete
    if states is not None:
        for state in states:
            session.delete(state)
    session.commit()

    session.close()
