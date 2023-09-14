#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    username, password, database = tuple(sys.argv[1:])
    db = MySQLdb.connect("localhost", username, password, database, port=3306)
    cursor = db.cursor()
    query = "SELECT * FROM cities ORDER BY id;"
    cursor.execute(query)
    table = cursor.fetchall()
    for row in table:
        print(row)
    cursor.close()
    db.close()
