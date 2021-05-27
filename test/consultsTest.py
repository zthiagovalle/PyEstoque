import sqlite3
import json
import os
import zipfile as zip


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

def getJson():
    con = sqlite3.connect('../database/db.db')
    list = con.execute(f'select * from produto where usuario_id=1').fetchall()
    print(list)
    input("Tecle enter")
    dic = getProduct(list)
    print(dic)
    input("Tecle enter")
    file = open("../export/Produtos.json", "w")
    json.dump(dic, file, indent=4)
    file.close()

def getProduct(productList):
    lstProductDic = []
    for product in productList:
        productDic = {'id':product[0], 'nome':product[1], 'valor_venda':product[2], 'valor_compra':product[3], 'quantidade_estoque':product[4], 'fornecedor_id':product[5], 'usuario_id':product[6]}
        lstProductDic.append(productDic)
    return lstProductDic

def compress(): 
    path_zip = os.path.join(os.sep,  os.getcwd().replace("test", "export"), "export.zip")
    path_dir = os.path.join(os.sep, os.getcwd().replace("test", ''), "export")

    zf = zip.ZipFile(path_zip, "w")
    for dirname, subdirs, files in os.walk(path_dir):
        for filename in files:
            if(filename.endswith('.json')):
                zf.write(os.path.join(dirname, filename))
    zf.close()

def readJson():
    datatotalProducts = []
    path_dir = os.path.join(os.sep, os.getcwd().replace("test", ''), "import")
    for dirname, subdirs, files in os.walk(path_dir):
        for filename in files:
            if(filename.endswith('Produtos.json')):
                with open(os.path.join(dirname, filename), 'r', encoding='utf8') as f:
                    data = json.load(f)
                    datatotalProducts.append(data)

    for data in datatotalProducts:
        print(data)

    datatotalProviders = []
    path_dir = os.path.join(os.sep, os.getcwd().replace("test", ''), "import")
    for dirname, subdirs, files in os.walk(path_dir):
        for filename in files:
            if(filename.endswith('Fornecedores.json')):
                with open(os.path.join(dirname, filename), 'r', encoding='utf8') as f:
                    data = json.load(f)
                    datatotalProviders.append(data)

    for data in datatotalProviders:
        print(data)

    input("tecle enter")

# getAllUsers()
# getAllProviders()
#getAllProducts()
#getProductsByProviderId(1, 1)
#getProducts(1)
#getJson()
#compress()
#readJson()