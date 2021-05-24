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

def getProducts(user_id_int):
    con = sqlite3.connect('../database/db.db')
    try:
        print(con.execute(f"""
        select f.nome, p.* 
        from produto as p, fornecedor as f
        where p.usuario_id={user_id_int} 
        and f.id = p.fornecedor_id
        order by p.nome
        """).fetchall())
    except :
        print("Erro")

# getAllUsers()
# getAllProviders()
#getAllProducts()
#getProductsByProviderId(1, 1)
getProducts(1)