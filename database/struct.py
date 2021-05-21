import os
import sqlite3
import utils.ClearPrompt as prompt

def create():
    prompt.clear()
    exist = False

    if os.path.isfile('./database/db.db'):
        exist = True

    if (exist == False):
        con = sqlite3.connect('./database/db.db')
        con.execute("""
        create table if not exists usuario(
                id integer not null primary key autoincrement,
                login text not null unique,
                nome text not null,
                senha text not null
            );""")

        con.execute("""
        create table if not exists fornecedor(
                id integer not null primary key autoincrement,
                nome text not null,
                telefone text not null,
                endereco text not null,
                usuario_id,

                foreign key(usuario_id) references usuario(id)
            )
            """)

        con.execute("""
        create table if not exists produto(
                id integer not null primary key,
                nome text not null,
                valor_venda float,
                valor_compra text,
                codigo_barras integer,
                quantidade_estoque integer,
                fornecedor_id integer,
                usuario_id integer,

                foreign key(fornecedor_id) references fornecedor(id)
                foreign key(usuario_id) references usuario(id)
            );
            """)

        con.commit()
        print("Banco de dados criado com sucesso !")
        input("tecle entrar para continuar..")

    else:
        print("O Banco de dados já está criado !")
        input("tecle entrar para continuar..")
