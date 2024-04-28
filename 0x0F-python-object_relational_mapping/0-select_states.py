#!/usr/bin/python3

import MySQLdb

from sys import argv



if __name__ == '__main':

    data = MySQLdb.connect(host="localhost" , port=3306, user=argv[1],passwd=argv[2], data=argv[3])

    tuto = data.cursor()
    tuto.execute("SELECT * FROM states")

    row = tuto.fetchall()
    for p in row:
        print(i)
    tuto.close()
    data.close()
