#!/usr/bin/python3
"""script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cr = db.cursor()
    myQuery = " ".join([
        "SELECT * FROM states",
        "WHERE name LIKE BINARY '{}'",
        "ORDER BY states.id",
        ]).format(sys.argv[4])
    cr.execute(myQuery)
    res = cr.fetchone()
    print(res)
    cr.close()
    db.close()
