from furiadb import get_connection

def listar_estatisticas(nickname):
    try:
        com = get_connection()
        cur = com.cursor()

        cur.execute("""
            SELECT j.nickname, j.nome_completo, j.nacionalidade, j.funcao,
                   e.rating, e.kd_diff, e.dpr, e.kast, e.impacto, e.adr
            FROM jogadores j
            JOIN estatisticas e ON j.id = e.jogador_id
            WHERE j.nickname = ?
        """, (nickname,))
        
        estatistica = cur.fetchone()
        
        if not estatistica:
            return None
        
        nick, nome, pais, funcao, rating, kd_diff, dpr, kast, impacto, adr = estatistica
        
        texto = (
            f"📊 Estatísticas de {nick} ({nome}):\n"
            f"🌍 Nacionalidade: {pais}\n"
            f"🔫 Função: {funcao}\n\n"
            f"⭐ Rating: {rating}\n"
            f"🔫 K/D Diff: {kd_diff}\n"
            f"🛡️ DPR: {dpr}\n"
            f"🎯 KAST: {kast}%\n"
            f"💥 Impacto: {impacto}\n"
            f"🔥 ADR: {adr}"
        )
        
        return texto
        
    except Exception as e:
        print(f"Erro ao buscar estatísticas: {e}")
        return None
    finally:
        if 'com' in locals():
            com.close()