import os
import sqlite3

def existUser(login):
    con = sqlite3.connect('./database/db.db')
    try:
        if(con.execute("select count(*) as existe from usuario where login=?", [login]).fetchone()[0] == 1):
            return True
        else:
            return False
    except:
        print("Ocorreu um erro na consulta.")

    
