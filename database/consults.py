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
