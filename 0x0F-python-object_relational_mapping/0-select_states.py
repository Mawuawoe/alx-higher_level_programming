#!/usr/bin/python3

import MySQLdb
import sys

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
         ORDER BY id;"""

cursor.execute(sql)

results = cursor.fetchall()
for row in results:
    print(row)

db.close()
