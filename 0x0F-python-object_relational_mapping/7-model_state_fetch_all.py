#!/usr/bin/python3
"""
a script that creating a table in a database
it take the user, passwd and database name as
cmd line arg
"""

from sqlalchemy import create_engine
from model_state import Base, State
import sys
from urllib.parse import quote_plus
from sqlalchemy.orm import sessionmaker

# Connect & Create tables
if __name__ == "__main__":
    """
    connect to database and create Table
    """
    user = sys.argv[1]
    # URL encode the password
    password = quote_plus(sys.argv[2])
    db = sys.argv[3]

    db_url = f'mysql+mysqldb://{user}:{password}@localhost/{db}'
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all()
    i = 1
    for state in states:
        print(f'{i}: {state.name}')
        i = i + 1
