#!/usr/bin/python3
"""a script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    username, password, database = tuple(sys.argv[1:])
    db = MySQLdb.connect("localhost", username, password, database, port=3306)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name COLLATE utf8mb4_bin LIKE 'N%';"
    cursor.execute(query)
    table = cursor.fetchall()
    for row in table:
        print(row)
    cursor.close()
    db.close()
