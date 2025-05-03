from furiadb import get_connection  

def adicionar_partida():
    try:
        com = get_connection()
        cursor = com.cursor()

        partida = {
            'data': '10-05-2025',
            'hora': '05:00',
            'time1': 'The MongolZ',  
            'time2': 'FURIA',        
            'formato': 'MD3',        
            'campeonato': 'PGL Astana 2025',  
            'link_transmissao': 'https://www.twitch.tv/pgl',  
            'mapa1': None,  
            'mapa2': None,
            'mapa3': None,
            'placar_time1': None,
            'placar_time2': None
        }

        cursor.execute("""
            INSERT INTO partidas (
                data, hora, time1, time2, formato, campeonato, link_transmissao,
                mapa1, mapa2, mapa3, placar_time1, placar_time2
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, tuple(partida.values()))

        com.commit()
        print(" Partida adicionada com sucesso!")

    except Exception as e:
        print(f" Erro ao adicionar partida: {e}")
    finally:
        if 'com' in locals():
            com.close()

if __name__ == "__main__":
    adicionar_partida()  