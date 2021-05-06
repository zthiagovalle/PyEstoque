import sqlite3
import os
import interfaces.menu
import database.criarTabela as criarTabela
criarTabela.criar()

interfaces.menu.main()
