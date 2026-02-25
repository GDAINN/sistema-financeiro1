import sqlite3 as lite
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "dados.db")

con = lite.connect(DB_PATH)

with con:
    cur = con.cursor()

    # tabela categoria
    cur.execute("""
        CREATE TABLE IF NOT EXISTS categoria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    """)

    # tabela receitas
    cur.execute("""
        CREATE TABLE IF NOT EXISTS receitas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria_id INTEGER,
            adicionado_em TEXT,
            valor REAL,
            FOREIGN KEY (categoria_id) REFERENCES categoria(id)
        )
    """)

    # tabela gastos
    cur.execute("""
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria_id INTEGER,
            retirado_em TEXT,
            valor REAL,
            FOREIGN KEY (categoria_id) REFERENCES categoria(id)
        )
    """)

#Inserir categoria
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO categoria (nome) VALUES (?)"
        cur.execute(query, i)

#Inserir_receitas
def inserir_receitas(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO receitas (categoria_id, adicionado_em, valor) VALUES (?,?,?)"
        cur.execute(query,i)

#Inserir_gastos
def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO gastos (categoria_id, retirado_em, valor) VALUES (?,?,?)"
        cur.execute(query,i)

# funções para deletar ....................................

#deletar Receitas
def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM receitas WHERE id=?"
        cur.execute(query,i)


#deletar Gastos
def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM gastos WHERE id=?"
        cur.execute(query,i)

#funções para ver dados............................

#ver categoria
def ver_categoria():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM categoria")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens


#ver receitas
def ver_receitas():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM receitas")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens


#ver gastos
def ver_gastos():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM gastos")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens


