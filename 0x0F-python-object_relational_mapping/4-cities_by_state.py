#!/usr/bin/python3
"""
A script that
that lists all cities from the database hbtn_0e_4_usa
JOIN data from the states table
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
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id;
    """
    cursor.execute(sql)

    results = cursor.fetchall()
    for row in results:
        print(row)

    db.close()
