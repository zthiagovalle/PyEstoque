import sqlite3

error = 'Ocorreu um erro na consulta.'

def existUser(login):
    con = sqlite3.connect('./database/db.db')
    try:
        if(con.execute(f'select count(*) from usuario where login="{login}"').fetchone()[0] == 1):
            return True
        else:
            return False
    except :
        print(error)

def authenticate(login, password):
    con = sqlite3.connect('./database/db.db')
    try:
        if(con.execute(f'select count(*) from usuario where login="{login}" and senha="{password}"').fetchone()[0] == 1):
            return True
        else:
            return False
    except :
        print(error)

def getIdByLogin(login):
    con = sqlite3.connect('./database/db.db')
    try:
        return con.execute(f'select id from usuario where login="{login}"').fetchone()[0]
    except :
        print(error)

def getProviders(login):
    con = sqlite3.connect('./database/db.db')
    user_id = getIdByLogin(login)
    user_id_int = int(user_id)
    try:
        return con.execute(f'select * from fornecedor where usuario_id={user_id_int} order by nome').fetchall()
    except :
        print(error)

def getProviderById(id, login):
    user_id = getIdByLogin(login)
    user_id_int = int(user_id)
    providerId = int(id)
    con = sqlite3.connect('./database/db.db')
    try:
        return con.execute(f'select * from fornecedor where id={providerId} and usuario_id={user_id_int}').fetchall()
    except :
        print(error)

def getProductById(id, login):
    user_id = getIdByLogin(login)
    user_id_int = int(user_id)
    con = sqlite3.connect('./database/db.db')
    try:
        return con.execute(f'select * from produto where id={id} and usuario_id={user_id_int}').fetchall()
    except :
        print(error)

def getProductsByProviderId(provider_id, login):
    user_id = getIdByLogin(login)
    user_id_int = int(user_id)
    con = sqlite3.connect('./database/db.db')
    try:
        return con.execute(f'select * from produto where fornecedor_id={provider_id} and usuario_id={user_id_int}').fetchall()
    except :
        print(error)

def getProducts(login):
    con = sqlite3.connect('./database/db.db')
    user_id = getIdByLogin(login)
    user_id_int = int(user_id)
    try:
        return con.execute(f"""
        select f.nome, p.* 
        from produto as p, fornecedor as f
        where p.usuario_id={user_id_int} 
        and f.id = p.fornecedor_id
        order by p.nome
        """).fetchall()
    except :
        print(error)