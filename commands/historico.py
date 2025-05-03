from furiadb import get_connection

def buscar_historico(limit=10):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT DISTINCT data, adversario, resultado, placar
    FROM historico_partidas
    ORDER BY data DESC
    LIMIT ?
    """, (limit,))
    
    partidas = cursor.fetchall()
    conn.close()
    return partidas

def formatar_historico(partidas):
    if not partidas:
        return "📭 *Nenhuma partida no histórico ainda!*"
    
    texto = " *HISTÓRICO DE BATALHAS* \n\n"
    
    for data, adversario, resultado, placar in partidas:
        if resultado == '✅':
            status_emoji = "🟢 VITÓRIA"
            trofeu = "🏆"
        else:
            status_emoji = "🔴 DERROTA"
            trofeu = "💥"
        
        if ":" in placar:
            placar_formatado = f"⚔️ *{placar.replace(':', '-')}*"
        else:
            placar_formatado = f"🔮 *{placar}*"
        
        texto += (
            f"{trofeu} *{data}* vs {adversario}\n"
            f"{placar_formatado} | {status_emoji}\n"
            f"───────────────────────\n"
        )
    
  
    return texto