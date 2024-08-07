#!/usr/bin/python3
"""
a script that creating a table in a database
it take the user, passwd and database name as
cmd line arg
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
import sys
from urllib.parse import quote_plus

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

    Base = declarative_base()

    class State(Base):
        """
        create Table
        """
        __tablename__ = "states"

        id = Column(Integer, autoincrement=True,
                    primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)

    Base.metadata.create_all(engine)
