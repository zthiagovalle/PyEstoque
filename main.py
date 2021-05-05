import sqlite3
import os
import interfaces.menu

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

    con.commit()

interfaces.menu.main()