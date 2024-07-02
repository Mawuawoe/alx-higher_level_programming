#!/usr/bin/python3
"""
a script that lists
all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
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
    sql = """SELECT *
             FROM states
             WHERE name LIKE 'N%';"""

    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)

    db.close()
