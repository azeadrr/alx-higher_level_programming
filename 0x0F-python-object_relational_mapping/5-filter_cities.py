#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all city"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    lines = cur.fetchall()
    tmp = list(line[0] for line in lines)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
