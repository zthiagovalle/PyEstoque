import sqlite3

error = 'Ocorreu um erro na alteração!'

def changePassword(login, newPassword):
    con = sqlite3.connect('./database/db.db')
    try:
        con.execute(f'update usuario set senha = "{newPassword}" where login = "{login}"')
        con.commit()
    except:
        print(error)

def changeProvider(id, newName, newPhoneNumber, newAddress):
    con = sqlite3.connect('./database/db.db')
    try:
        con.execute(f'update fornecedor set nome= "{newName}", telefone="{newPhoneNumber}", endereco="{newAddress}" where id = {id}')
        con.commit()
    except:
        print(error)

def changeProduct(id, newName, newPurchasePrice, newSalePrice, stokQuantity):
    con = sqlite3.connect('./database/db.db')
    try:
        con.execute(f'update produto set nome= "{newName}", valor_venda="{newSalePrice}", valor_compra="{newPurchasePrice}", quantidade_estoque ={stokQuantity} where id = {id}')
        con.commit()
    except:
        print(error)