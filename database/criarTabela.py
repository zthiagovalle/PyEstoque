import os
import sqlite3


def criar():
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
                endereco text not null
            )
            """)

        con.execute("""
        create table if not exists categoria(
                id integer not null primary key,
                categoria text not null unique
            );
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
                categoria_id integer,

                foreign key(categoria_id) references categoria(id)

                foreign key(fornecedor_id) references fornecedor(id)
            );
            """)

        con.execute("""
        create table if not exists venda(
                id integer not null primary key,
                valor_total integer not null,
                data_venda integer not null
            );
            """)

        con.execute("""
        insert into 
            categoria 
            (categoria) 
        values 
            ("danone"),("sorvete"),("arroz"),("feijão")""")
        con.execute("""
        insert into 
            fornecedor 
            (nome,telefone,endereco) 
        values 
            ("Fornecedor 1","161111","R Palmares, 423"),
            ("Fornecedor 2","162222","Av Limao, 7")""")
        con.execute("""
        insert into 
            usuario 
            (login, nome, senha) 
        values 
            ("thiago","Thiago","321"),
            ("gabriel","Gabriel","123")""")
        con.execute("""
        insert into 
            produto 
            (nome, valor_venda, valor_compra, codigo_barras, quantidade_estoque, fornecedor_id, categoria_id) 
        values 
            ('Yakult', 5, 4.5, '1', 10, 1, 1), 
            ('Kibom', 19, 10, '2', 2, 1, 2)""")

        con.commit()
