#!/usr/bin/python3
"""
a script that list the content of a table in a database
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
    connect to database
    list all states in ASC order
    """
    user = sys.argv[1]
    # URL encode the password
    password = quote_plus(sys.argv[2])
    db = sys.argv[3]

    db_url = f'mysql+mysqldb://{user}:{password}@localhost/{db}'
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()

session.close()
