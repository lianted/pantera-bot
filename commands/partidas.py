from furiadb import get_connection

def listar_proximas_partidas():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT DISTINCT data, hora, time1, time2, formato, campeonato, link_transmissao
    FROM partidas
    WHERE placar_time1 IS NULL
    ORDER BY data, hora
    """)
    
    partidas = cursor.fetchall()
    conn.close()
    return partidas

def formatar_partidas(partidas):
    if not partidas:
        return "📅 Não há partidas agendadas no momento."
    
    texto = "🎮 **Próximas BATALHAS**\n\n"
    for partida in partidas:
        data, hora, time1, time2, formato, campeonato, link = partida
        texto += (
            f"💥 **{time1} vs {time2}**\n"
            f"📅 {data} às {hora}\n"
            f"🏆 {campeonato} | 🎯 {formato}\n"
            f"🔗 [Assistir na Twitch]({link})\n\n"
        )
    return texto