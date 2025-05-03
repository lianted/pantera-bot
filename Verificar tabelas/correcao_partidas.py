from furiadb import get_connection

def atualizar_estrutura_tabela():
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS partidas_temp AS
        SELECT * FROM partidas
        """)
        
        
        cursor.execute("DROP TABLE partidas")
        
        cursor.execute("""
        CREATE TABLE partidas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            hora TEXT NOT NULL,
            time1 TEXT NOT NULL,
            time2 TEXT NOT NULL,
            formato TEXT NOT NULL,
            campeonato TEXT NOT NULL,
            link_transmissao TEXT,
            mapa1 TEXT,
            mapa2 TEXT,
            mapa3 TEXT,
            placar_time1 INTEGER,
            placar_time2 INTEGER
        )
        """)
        
       
        cursor.execute("""
        INSERT INTO partidas (data, campeonato)
        SELECT data, torneio FROM partidas_temp
        """)
        
       
        cursor.execute("DROP TABLE partidas_temp")
        
        conn.commit()
        print("Estrutura da tabela atualizada com sucesso!")
        
    except Exception as e:
        conn.rollback()
        print(f"Erro ao atualizar tabela: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    atualizar_estrutura_tabela()