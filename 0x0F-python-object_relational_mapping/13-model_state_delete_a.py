#!/usr/bin/python3
"""
A script that deletes all State objects
from a database that contain the letter 'a'.
It takes the user, password, and database name as command line arguments.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
from urllib.parse import quote_plus

BATCH_SIZE = 100  # Number of records to process in each batch

if __name__ == "__main__":
    """
    Connect to database and delete states containing the letter 'a'
    """
    user = sys.argv[1]
    # URL encode the password
    password = quote_plus(sys.argv[2])
    db = sys.argv[3]

    db_url = f'mysql+mysqldb://{user}:{password}@localhost/{db}'
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Fetch and delete states in batches
        while True:
            states = session.query(State)\
                .filter(State.name.like('%a%')).limit(BATCH_SIZE).all()
            if not states:
                break
            for state in states:
                session.delete(state)
            session.commit()

    except Exception:
        session.rollback()
    finally:
        # Close the session
        session.close()
