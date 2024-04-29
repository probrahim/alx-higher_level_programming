#!/usr/bin/python3
"""print states from database"""
import MySQLdb

import sys


def tuto():
    data = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            charset="utf8")
    mycursor = data.cursor()
    mycursor.execute("""SELECT * FROM states
                        WHERE BINARY name LIKE 'N%' ORDER BY id ASC""")

    result = mycursor.fetchall()
    for row in result:
        print(row)


if __name__ == "__main__":
    tuto()
