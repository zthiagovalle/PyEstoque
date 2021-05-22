import sqlite3
import database.consults as consults

error = 'Ocorreu um erro na exclusão!'

def deleteAccount(login):
    con = sqlite3.connect('./database/db.db')
    try:
        user_id = consults.getIdByLogin(login)
        user_id_int = int(user_id)
        con.execute(f'delete * from usuario where login = "{login}"')
        con.execute(f'delete * from produto where usuario_id = {user_id_int}')
        con.execute(f'delete * from fornecedor where usuario_id = {user_id_int}')
        con.commit()
    except:
        print(error)