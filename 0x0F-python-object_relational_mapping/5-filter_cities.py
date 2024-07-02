#!/usr/bin/python3
"""
A script that
takes in the name of a state as an argument and
lists all cities of that state,
using the database hbtn_0e_4_usa
Dallas, Houston, Austin
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Connect to the database
    """
    username = sys.argv[1]
    userpasswd = sys.argv[2]
    dbname = sys.argv[3]
    stateName = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=userpasswd,
        db=dbname,
        port=3306  # Optional, default is 3306
    )

    cursor = db.cursor()

    # Use parameterized query to prevent SQL injection
    sql = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = BINARY %s;"""

    cursor.execute(sql, (stateName,))

    results = cursor.fetchall()
    city_names = [row[0] for row in results]
    print(", ".join(city_names))

    db.close()
