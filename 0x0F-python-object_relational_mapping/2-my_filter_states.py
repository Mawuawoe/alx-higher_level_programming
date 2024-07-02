#!/usr/bin/python3
"""
A script that takes in arguments and
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    connect to the database
    print all content of the state table
    that start with N
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

    stateName = sys.argv[4]

    sql = "SELECT * FROM states WHERE name = BINARY '{}';".format(stateName)

    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)

    db.close()
