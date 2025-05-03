import sqlite3

def atualizar_estatisticas():
    
    estatisticas_jogadores = [
        ("FalleN", 1.04, 1, 0.71, 69.8, 1.02, 71.3),
        ("yuurih", 1.16, 12, 0.65, 73.2, 1.08, 81.3),
        ("KSCERATO", 1.13, 8, 0.68, 72.5, 1.01, 77.9),
        ("molodoy", 0.98, -3, 0.75, 69.1, 0.90, 68.5),
        ("YEKINDAR", 1.05, 2, 0.72, 70.4, 1.06, 74.1)
    ]
    
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    
    for nick, rating, kd_diff, dpr, kast, impacto, adr in estatisticas_jogadores:
        cursor.execute("SELECT id FROM jogadores WHERE nickname = ?", (nick,))
        result = cursor.fetchone()
        
        if result:
            jogador_id = result[0]
            cursor.execute("SELECT 1 FROM estatisticas WHERE jogador_id = ?", (jogador_id,))
            
            if cursor.fetchone():
                
                cursor.execute("""
                    UPDATE estatisticas 
                    SET rating = ?,
                        kd_diff = ?,
                        dpr = ?,
                        kast = ?,
                        impacto = ?,
                        adr = ?
                    WHERE jogador_id = ?
                """, (rating, kd_diff, dpr, kast, impacto, adr, jogador_id))
            else:
              
                cursor.execute("""
                    INSERT INTO estatisticas 
                    (jogador_id, rating, kd_diff, dpr, kast, impacto, adr)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (jogador_id, rating, kd_diff, dpr, kast, impacto, adr))
        else:
            print(f"Jogador {nick} não encontrado no banco de dados!")
    
    conn.commit()
    conn.close()
    print("Estatísticas atualizadas com sucesso!")


atualizar_estatisticas()