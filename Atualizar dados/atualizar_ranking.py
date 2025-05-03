import sqlite3
from datetime import datetime

def atualizar_ranking_completo():
    ranking_data = [
        (1, "Vitality", 1000),
        (2, "Spirit", 645),
        (3, "MOUZ", 582),
        (4, "Natus Vincere", 431),
        (5, "Aurora", 413),
        (6, "The MongolZ", 407),
        (7, "G2", 388),
        (8, "Falcons", 341),
        (9, "FaZe", 269),
        (10, "Liquid", 199),
        (11, "GamerLegion", 198),
        (12, "Virtus.pro", 186),
        (13, "3DMAX", 166),
        (14, "Complexity", 129),
        (15, "Astralis", 92),
        (16, "paiN", 78),
        (17, "FURIA", 68)
    ]
    
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    
    
    data_mudanca = datetime.now().strftime('%d-%m-%Y')
    
    
    cursor.execute("UPDATE ranking SET posicao = 999")
    
   
    for posicao, time, pontos in ranking_data:
        cursor.execute("""
            UPDATE ranking 
            SET posicao = ?, pontos = ?, mudanca = ?
            WHERE time = ?
        """, (posicao, pontos, data_mudanca, time))
        
     
        if cursor.rowcount == 0:
            cursor.execute("""
                INSERT INTO ranking (posicao, time, pontos, mudanca)
                VALUES (?, ?, ?, ?)
            """, (posicao, time, pontos, data_mudanca))
    
   
    cursor.execute("""
        DELETE FROM ranking 
        WHERE posicao = 999 AND mudanca != ?
    """, (data_mudanca,))
    
    conn.commit()
    conn.close()
    print("Ranking atualizado com sucesso para os 17 times!")


atualizar_ranking_completo()