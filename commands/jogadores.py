from furiadb import get_connection

def listar_jogadores():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT DISTINCT nickname, nome_completo, nacionalidade, data_entrada, funcao FROM jogadores")
    jogadores = cur.fetchall()
    conn.close()    
    

    print("=== DADOS BRUTOS DO BANCO ===")
    
    for j in jogadores:
        print(repr(j))

    texto = "🔥 JOGADORES DA FÚRIA 🔥\n\n"
    texto += "⚡ Lista de Ativos ⚡\n"
    texto += "―――――――――――――――――――――――――――\n\n"

    bandeiras = {
        "brazil": "🇧🇷",
        "latvia": "🇱🇻",
        "kazakhstan": "🇰🇿",
    }

    for j in jogadores:
        nickname, nome, nacionalidade, entrada, funcao = j
        
        print(f"\nOriginal: '{nacionalidade}'")
        nacionalidade_clean = nacionalidade.strip().lower()
        print(f"Limpo: '{nacionalidade_clean}'")
        
        bandeira = bandeiras.get(nacionalidade_clean, "🌎")
        print(f"Bandeira encontrada: {bandeira}")

        if "entry fragger" in funcao.lower():
            emoji_funcao = "⚔️"
        elif "lurker" in funcao.lower():
            emoji_funcao = "👁️"
        elif "in game leader" in funcao.lower() or "igl" in funcao.lower():
            emoji_funcao = "🧠" 
        elif "awper" in funcao.lower():
            emoji_funcao = "🎯"
        elif "rifler" in funcao.lower():
            emoji_funcao = "🔫"
        else:
            emoji_funcao = "🛡️"

        texto += (
            f"👤 {nickname} ({nome})\n"
            f"{bandeira} {nacionalidade}\n"
            f"{emoji_funcao} {funcao}\n" 
            f"📅 Entrou em: {entrada}\n"
            f"――――――――――――――――――――――――――\n"
        )
    
    texto += "\n💥 Força Fúria! 💥"
    return texto