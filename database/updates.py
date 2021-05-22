import sqlite3

error = 'Ocorreu um erro na alteração!'

def changePassword(login, newPassword):
    con = sqlite3.connect('./database/db.db')
    try:
        con.execute(f'update usuario set senha = "{newPassword}" where login = "{login}"')
        con.commit()
    except:
        print(error)