import sqlite3

def getAllUsers():
    con = sqlite3.connect('../database/db.db')
    print(con.execute('select * from usuario').fetchall())

def getAllProviders():
    con = sqlite3.connect('../database/db.db')
    print(con.execute('select * from fornecedor').fetchall())

def getAllProducts():
    con = sqlite3.connect('../database/db.db')
    print(con.execute('select * from produto').fetchall())

def getProductsByProviderId(providerId, user_id):
    con = sqlite3.connect('../database/db.db')
    print(con.execute(f'select * from produto where fornecedor_id={providerId} and usuario_id={user_id}').fetchall())

getAllUsers()
getAllProviders()
getAllProducts()
getProductsByProviderId(1, 1)