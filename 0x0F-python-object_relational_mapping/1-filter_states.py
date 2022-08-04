#!/usr/bin/python3
"""script that lists all states with a name
starting with N from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cr = db.cursor()
    cr.execute("SELECT * FROM states
               WHERE name REGEXP '^N'
               ORDER BY states.id")
    res = cr.fetchall()
    for rows in res:
        print(rows)
    cr.close()
    db.close()
