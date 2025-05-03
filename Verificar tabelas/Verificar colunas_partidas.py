from furiadb import get_connection

def verificar_colunas():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("PRAGMA table_info(partidas)")
    colunas = [col[1] for col in cursor.fetchall()]
    
    conn.close()
    print("Colunas existentes na tabela partidas:", colunas)

verificar_colunas()