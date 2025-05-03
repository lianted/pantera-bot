from furiadb import get_connection

def add_historico(data, campeonato, resultado, placar, adversario):
    """Adiciona uma partida ao histórico - SIMPLES E DIRETO"""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
        INSERT INTO historico_partidas 
        (data, campeonato, resultado, placar, adversario)
        VALUES (?, ?, ?, ?, ?)
        """, (data, campeonato, resultado, placar, adversario))
        
        conn.commit()
        print(f"✅ Added: {data} vs {adversario}")
    except Exception as e:
        print(f"❌ Falha: {e}")
    finally:
        conn.close()

# Dados iniciais (igual ao seu exemplo)
PARTIDAS = [
    ("09/04/2025", "PGL Bucharest 2025", "❌", "0:2", "MongolZ"),
    ("08/04/2025", "PGL Bucharest 2025", "❌", "0:2", "VP"),
    ("07/04/2025", "PGL Bucharest 2025", "❌", "1:2", "COL"),
    ("06/04/2025", "PGL Bucharest 2025", "✅", "2:0", "Apogee"),
    ("22/03/2025", "BLAST Open Spring 2025", "❌", "1:2", "M80")
]

if __name__ == "__main__":
    for p in PARTIDAS:
        add_historico(*p)
    print("Histórico atualizado!")