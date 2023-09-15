#!/usr/bin/python3
"""a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    username, password, database, state = tuple(sys.argv[1:])
    db = MySQLdb.connect("localhost", username, password, database, port=3306)
    cursor = db.cursor()
    query = "SELECT c.name FROM cities c INNER JOIN states s " + \
        "ON  s.id = c.state_id WHERE s.name = %s  ORDER BY c.id;"
    cursor.execute(query, (state, ))
    table = cursor.fetchall()
    i = 0
    while i < len(table):
        print(table[i][0], end=", " if i != len(table) - 1 else "\n")
        i += 1
    cursor.close()
    db.close()
