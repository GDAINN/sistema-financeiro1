#importando SQLite

import sqlite3 as lite

#Criando conexão
con = lite.connect('dados.db')

# funções de Inserção......................................

#Inserir categoria
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query,i)

#Inserir_receitas
def inserir_receitas(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO receitas (categoria, adicionado_em, valor) VALUES (?,?,?)"
        cur.execute(query,i)

#Inserir_gastos
def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO gastos (categoria, retirado_em, valor) VALUES (?,?,?)"
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


