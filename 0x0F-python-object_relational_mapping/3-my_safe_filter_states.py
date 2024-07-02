#!/usr/bin/python3
"""
A script that takes in arguments and
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
But this time, write one that is safe from MySQL injections!
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
    sql = "SELECT * FROM states WHERE name = BINARY %s;"
    cursor.execute(sql, (stateName,))

    results = cursor.fetchall()
    for row in results:
        print(row)

    db.close()
