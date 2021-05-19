import sqlite3

def getAllUsers():
    con = sqlite3.connect('../database/db.db')
    print(con.execute('select * from usuario').fetchall())

getAllUsers()
