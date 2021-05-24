import sqlite3
import database.consults as consults

error = 'Ocorreu um erro na inserção!'

def createUser(name, login, password):
    con = sqlite3.connect('./database/db.db')
    try:
        con.execute(f'insert into usuario (nome, login, senha) values ("{name}", "{login}", "{password}")')
        con.commit()
    except:
        print(error)

def createProvider(login, name, phoneNumber, address):
    con = sqlite3.connect('./database/db.db')
    try:
        user_id = consults.getIdByLogin(login)
        user_id_int = int(user_id)
        con.execute(f'insert into fornecedor (nome, telefone, endereco, usuario_id) values ("{name}", "{phoneNumber}", "{address}", {user_id_int})')
        con.commit()
        return True
    except:
        print(error)
        return False

def createProduct(login, providerId, name, purchasePrice, salePrice):
    con = sqlite3.connect('./database/db.db')
    try:
        user_id = consults.getIdByLogin(login)
        user_id_int = int(user_id)
        con.execute(f'insert into produto (nome, valor_venda, valor_compra, quantidade_estoque, fornecedor_id, usuario_id) values ("{name}", "{salePrice}", "{purchasePrice}", 0, {providerId} ,{user_id_int})')
        con.commit()
        return True
    except:
        print(error)
        return False