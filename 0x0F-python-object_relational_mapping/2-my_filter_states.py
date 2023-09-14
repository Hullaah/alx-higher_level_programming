#!/usr/bin/python3
"""a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    username, password, database, state = tuple(sys.argv[1:])
    db = MySQLdb.connect("localhost", username, password, database, port=3306)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id;"
    cursor.execute(query.format(state))
    table = cursor.fetchall()
    for row in table:
        print(row)
    cursor.close()
    db.close()
