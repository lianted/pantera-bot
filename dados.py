from furiadb import get_connection, init_db

def inserir_dados():
    conn = get_connection()
    cur = conn.cursor()

    jogadores = [
        ("yuurih", "Yuri Boian", "Brasil", "2017-11-08", "Rifler"),
        ("KSCERATO", "Kaike Cerato", "Brasil", "2018-02-06", "Rifler Lurker"),
        ("FalleN", "Gabriel Toledo", "Brasil", "2023-07-03", "IGL"),
        ("molodoy", "Danil Golubenko", "Kazakhstan", "2025-04-11", "AWPer"),
        ("YEKINDAR", "Mareks Gaļinskis", "Latvia", "2025-04-22", "Rifler Entry Fragger"),
        ("sidde", "Sidnei Macedo", "Brasil", "2024-07-09", "Coach")
    ]
    
    campeonatos = [
        ("1st", "A-Tier", "Elisa Masters Espoo 2023", "3:1", "$100,000"),
        ("3rd - 4th", "S-Tier", "Intel Extreme Masters Rio Major 2022", "1:2", "$80,000"),
        ("3rd - 4th", "S-Tier", "ESL Pro League Season 15", "0:2", "$55,000"),
        ("1st", "A-Tier", "Elisa Invitational Summer 2021", "2:1", "$50,000"),
        ("1st", "S-Tier", "ESL Pro League Season 12: North America", "3:0", "$77,500"),
        ("1st", "A-Tier", "DreamHack Masters Spring 2020: North America", "3:0", "$40,000"),
        ("1st", "A-Tier", "Arctic Invitational 2019", "2:0", "$66,519.41"),
        ("1st", "B-Tier", "EMF CS:GO World Invitational 2019", "3:1", "$63,951.50"),
        ("1st", "A-Tier", "ESEA Season 31: Global Challenge", "2:0", "$25,000"),
        ("2nd", "S-Tier", "Esports Championship Series Season 7 - Finals", "0:2", "$100,000"),
    ]


   
    ranking = [
        (1, "Vitality", 1000, "2025-04-28"),
        (2, "Spirit", 645, "2025-04-28"),
        (3, "MOUZ", 582, "2025-04-28"),
        (4, "Natus Vincere", 431, "2025-04-28"),
        (5, "Aurora", 413, "2025-04-28"),
        (6, "The MongolZ", 407, "2025-04-28"),
        (7, "G2", 383, "2025-04-28"),
        (8, "Falcons", 341, "2025-04-28"),
        (9, "FaZe", 269, "2025-04-28"),
        (10, "Liquid", 199, "2025-04-28"),
        (11, "GamerLegion", 198, "2025-04-28"),
        (12, "Virtus.pro", 186, "2025-04-28"),
        (13, "3DMAX", 166, "2025-04-28"),
        (14, "Complexity", 129, "2025-04-28"),
        (15, "Astralis", 92, "2025-04-28"),
        (16, "paiN", 78, "2025-04-28"),
        (17, "FURIA", 68, "2025-04-28"),
    ]

 



    cur.executemany("INSERT INTO jogadores (nickname, nome_completo, nacionalidade, data_entrada, funcao) VALUES (?, ?, ?, ?, ?)", jogadores)
    cur.executemany("INSERT INTO campeonatos (colocacao, tier, nome, resultado, premiacao) VALUES (?, ?, ?, ?, ?)", campeonatos)
    cur.executemany("INSERT INTO ranking (posicao, equipe, pontos, data) VALUES (?, ?, ?, ?)", ranking)
    
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()