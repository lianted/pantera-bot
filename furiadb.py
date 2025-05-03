import sqlite3

def get_connection():
    return sqlite3.connect('database.sqlite')

def init_db():
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
    CREATE TABLE IF NOT EXISTS jogadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nickname TEXT NOT NULL,
        nome_completo TEXT,
        nacionalidade TEXT,
        data_entrada TEXT,
        funcao TEXT
    )
    """)
    
        cursor.execute("""
    CREATE TABLE IF NOT EXISTS campeonatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        colocacao TEXT,
        tier TEXT,
        nome TEXT,
        resultado TEXT,
        premiacao TEXT
    )
    """)

        cursor.execute("""
    CREATE TABLE IF NOT EXISTS partidas (
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
CREATE TABLE IF NOT EXISTS estatisticas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    jogador_id INTEGER,
    rating REAL,
    kd_diff INTEGER,
    dpr REAL,
    kast REAL,
    impacto REAL,
    adr REAL,
    FOREIGN KEY(jogador_id) REFERENCES jogadores(id)
)
""")

        cursor.execute("""
CREATE TABLE IF NOT EXISTS ranking (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    posicao INTEGER,
    time TEXT,
    pontos INTEGER,
    mudanca TEXT
)
""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico_partidas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            campeonato TEXT NOT NULL,
            resultado TEXT NOT NULL,
            placar TEXT NOT NULL,
            adversario TEXT NOT NULL,
            mapa1 TEXT,
            mapa2 TEXT,
            mapa3 TEXT
        )
        """)
    
    
        conn.commit()
        print("Banco de dados inicializado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao inicializar banco de dados: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    init_db()