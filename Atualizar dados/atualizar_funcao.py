import sqlite3

def atualizar_funcao(nickname, nova_funcao):
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    
    cursor.execute("UPDATE jogadores SET funcao = ? WHERE nickname = ?", 
                  (nova_funcao, nickname))
    
    print(f"Linhas afetadas: {cursor.rowcount}")
    conn.commit()
    conn.close()

atualizar_funcao('yuurih', 'Rifler')
atualizar_funcao('KSCERATO', 'Rifler Lurker')
atualizar_funcao('FalleN', 'In Game Leader')
atualizar_funcao('molodoy', 'Awper')
atualizar_funcao('YEKINDAR', 'Rifler Entry Fragger')
