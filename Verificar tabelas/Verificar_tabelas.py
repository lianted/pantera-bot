import sqlite3

try:
    conn = sqlite3.connect("database.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tabelas = cur.fetchall()
    print("Tabelas existentes:", tabelas)
    conn.close()
except sqlite3.DatabaseError as e:
    print("Erro:", e)
