#!/usr/bin/python3
"""
A script that lists the contents of a table in a database.
It takes the user, password, and database name as command line arguments.
"""

from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
import sys
from urllib.parse import quote_plus
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the database and list all Cities
    """
    user = sys.argv[1]
    # URL encode the password
    password = quote_plus(sys.argv[2])
    db = sys.argv[3]

    db_url = f'mysql+mysqldb://{user}:{password}@localhost/{db}'
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).join(State).all()
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
