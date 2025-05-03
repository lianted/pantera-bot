from furiadb import get_connection

def listar_ranking():
    com = get_connection()
    cur = com.cursor()

    cur.execute("SELECT posicao, time, pontos, mudanca FROM ranking ORDER BY posicao LIMIT 17")
    ranking = cur.fetchall()
    com.close()

    texto = "🏆 RANKING DOS 17 PRIMEIROS COLOCADOS 🏆\n\n"
    texto += "📊 Posição  |  🏁 Time |  💯 Pontos  |  📈 Mudança\n"
    texto += "――――――――――――――――――――――――――――――――――\n"
    
    for r in ranking:
        posicao, time, pontos, mudanca = r
        
        try:
            mudanca_int = int(mudanca)
        except (ValueError, TypeError):
            mudanca_int = 0

        if posicao == 1:
            texto += f"🥇 #{posicao} | {time} | {pontos} pts | "
        elif posicao == 2:
            texto += f"🥈 #{posicao} | {time} | {pontos} pts | "
        elif posicao == 3:
            texto += f"🥉 #{posicao} | {time} | {pontos} pts | "
        else:
            texto += f"🔹 #{posicao} | {time} | {pontos} pts | "
        
        if mudanca_int > 0:
            texto += f"⬆️ +{mudanca_int}\n"
        elif mudanca_int < 0:
            texto += f"⬇️ {mudanca_int}\n"
        else:
            texto += f"➖ {mudanca_int}\n"
    
    return texto