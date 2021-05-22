import sqlite3

error = 'Ocorreu um erro na inserção!'

def createUser(name, login, password):
    con = sqlite3.connect('./database/db.db')
    try:
        con.execute(f'insert into usuario (nome, login, senha) values ("{name}", "{login}", "{password}")')
        con.commit()
    except:
        print(error)