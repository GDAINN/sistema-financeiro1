import sqlite3 as lite

# criando conexão
con = lite.connect('dados.db')

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
