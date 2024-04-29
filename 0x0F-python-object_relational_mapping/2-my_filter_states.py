#!/usr/bin/python3

import MySQLdb
import sys


def lalo():
    data = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    data_1 = data.cursor()

    data_1.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(sys.argv[4]))
    x = data_1.fetchall()

    for i in x:
        print(i)
    data_1.close()
    data.close()


if __name__ == "__main__":
    lalo()
