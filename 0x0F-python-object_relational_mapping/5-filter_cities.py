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
    data_1 = data.cursor()
    data_1.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))

    result = data_1.fetchall()
    for row in result:
        print(row)


if __name__ == "__main__":
    tuto()
