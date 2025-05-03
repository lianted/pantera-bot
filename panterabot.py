from email.mime import application
import os
import asyncio
import threading
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
from commands.jogadores import listar_jogadores
from commands.campeonatos import listar_campeonatos, formatar_campeonatos
from commands.ranking import listar_ranking
from commands.estatisticas import listar_estatisticas
from commands.partidas import listar_proximas_partidas, formatar_partidas
from commands.historico import buscar_historico, formatar_historico 


TOKEN = os.environ['TELEGRAM_TOKEN']

def print_banner():
    banner = """
    🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
    
    ███████╗██╗░░░██╗██████╗░██╗ ░█████╗░
    ██╔════╝██║░░░██║██╔══██╗██║ ██╔══██╗
    █████╗░░██║░░░██║██████╔╝██║ ███████║
    ██╔══╝░░██║░░░██║██╔══██╗██║ ██╔══██║
    ██║░░░░░╚██████╔╝██║░░██║██║ ██║░░██║
    ╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝
    
    ⚔️ Pantera News INICIADO COM SUCESSO! ⚔️
    📻 Bot pronto para transmitir a fúria!
    🕒 {hora_atual}
    
    🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
    """
    from datetime import datetime
    print(banner.format(hora_atual=datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

async def keep_alive():
    while True:
        try:
            requests.get('https://pantera-bot.up.railway.app')
            await asyncio.sleep(300)
        except Exception as e:
            print(f"Erro no keep-alive: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        "🤖 *BEM-VINDO AO PANTERA NEWS!* 🤖\n\n"
        "🔥 *O bot da torcida FURIOSA de CS2!* 🔥\n\n"
        
        "🎮 *COMANDOS PRINCIPAIS* 🎮\n\n"

         "👉[Loja Oficial](https://www.furia.gg/) - Vista o estilo FÚRIA, moda para quem vive o game! 🔥\n\n"
        
        "🟢 */start* - Mostra este menu de ajuda completo\n\n"

        "👥 */jogadores* - Lista completa do elenco com:\n"
        "      → Nickname, nome real e função\n"
        "      → Nacionalidade e data de contratação\n\n"
        
        "🏆 */ranking* - Ranking atual das equipes com:\n"
        "      → Posição, pontos e variação\n"
        "      → Top 17 equipes globais\n\n"
        
        "📅 */partidas* - Agenda de jogos com:\n"
        "      → Data/hora e formato da partida\n"
        "      → Campeonato e link para assistir\n\n"
        
        "📜 */historico* - Últimos resultados:\n"
        "      → Adversário e placar final\n"
        "      → Campeonato e desempenho (✅/❌)\n\n"
        
        "📊 */estatisticas* [nick] - Estatísticas detalhadas:\n"
        "      → Rating 2.0, K/D, ADR, KAST\n"
        "      → Impacto e desempenho por mapa\n"
        "      → Ex: /estatisticas KSCERATO\n\n"
        
        "🏆 /campeonatos - Histórico de títulos\n"
        "      → Títulos conquistados\n\n"

        "⚔️ /historia - Conheca a historia da FÚRIA!\n\n"
        
        "🌐 *LINKS IMPORTANTES* 🌐\n"
        "📺 [Twitch Oficial](https://www.twitch.tv/furiatv) - Transmissões ao vivo\n"
        "🐦 [X](https://x.com/FURIA) - Notícias em tempo real\n"
        "📸 [Instagram](https://www.instagram.com/furiagg/) - Bastidores do time\n\n"
        
        "⚙️ *Sugestões?* Mande uma mensagem para @lxxz\n\n"
        
        "⚔️ *NÃO APENAS ASSISTA - VIVA A FÚRIA!* ⚔️\n"
        "🔥 *A FÚRIA VAI TE PEGAR!* 🔥"

    )
    
    await update.message.reply_text(
        mensagem,
        parse_mode='Markdown',
        disable_web_page_preview=True
    )
async def historia(update: Update, context: CallbackContext) -> None:
    texto = (
        "*História da FURIA Esports*\n\n"
        "A FURIA foi fundada em agosto de 2017 por Jaime Pádua, um ex-advogado, e André Akkari, profissional de pôquer. "
        "O projeto nasceu com o propósito de construir uma organização brasileira que unisse alto desempenho competitivo "
        "com uma identidade de marca forte e uma cultura própria.\n\n"
        
        "Em 2018, a FURIA começou a ganhar notoriedade no cenário de Counter-Strike: Global Offensive (CS:GO), ao investir "
        "em jovens promessas como KSCERATO e yuurih. Em 2019, a equipe atingiu projeção internacional ao alcançar finais e "
        "top 3 em torneios como a DreamHack Masters Dallas. Isso consolidou a equipe entre as melhores do mundo.\n\n"
        
        "Entre 2020 e 2021, a FURIA se estabeleceu como uma potência. Com um estilo de jogo agressivo e criativo liderado "
        "por arT, a equipe figurou entre os cinco melhores times do mundo em diversos momentos. Além disso, lançou uma linha "
        "de roupas, abriu um centro de treinamento nos Estados Unidos e firmou sua identidade com o lema: 'FURIA é identidade.'\n\n"
        
        "Expandindo suas fronteiras, a organização ingressou em outros jogos como League of Legends (participando do CBLOL), "
        "Valorant, Rainbow Six Siege, Apex Legends e FIFA. Essa diversificação demonstrou o compromisso da FURIA em se tornar "
        "uma referência no cenário global dos esportes eletrônicos.\n\n"
        
        "Nos anos de 2022 e 2023, a equipe de CS:GO enfrentou oscilações, mas manteve-se relevante com a chegada de jogadores "
        "experientes como FalleN, chelo e saffee. A base formada por KSCERATO e yuurih se manteve como pilar da equipe.\n\n"
        
        "Com o lançamento do Counter-Strike 2, em 2024, a FURIA iniciou um novo ciclo. A organização permanece como uma das "
        "principais representantes do Brasil nos esports, tanto pelo desempenho quanto pela força da sua marca.\n\n"
        
        "Hoje, a FURIA é reconhecida internacionalmente não apenas por seus resultados, mas pela sua postura, visão de longo "
        "prazo e pela relação próxima com sua torcida. A frase 'FURIA é mais do que um time. É um movimento.' sintetiza a essência "
        "do projeto.\n"
    )
    await update.message.reply_text(texto, parse_mode='Markdown')

async def jogadores(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = listar_jogadores()
    await update.message.reply_text(texto)

async def campeonatos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        dados_campeonatos = listar_campeonatos()
        texto = formatar_campeonatos(dados_campeonatos)
        await update.message.reply_text(texto, parse_mode='Markdown')
    except Exception as e:
        print(f"Erro no comando /campeonatos: {e}")
        await update.message.reply_text("❌ Erro ao buscar campeonatos!")

async def ranking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = listar_ranking()
    await update.message.reply_text(texto)

async def estatisticas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if not context.args:
            await update.message.reply_text("⚠️ Por favor, informe o nickname do jogador.\nExemplo: /estatisticas FalleN")
            return
        
        nickname = ' '.join(context.args)
        texto = listar_estatisticas(nickname)
        
        if texto is None:
            await update.message.reply_text(f"❌ Jogador '{nickname}' não encontrado ou sem estatísticas cadastradas.")
        else:
            await update.message.reply_text(texto)            
    except Exception as e:
        print(f"Erro no handler de estatísticas: {e}")
        await update.message.reply_text("⚠️ Ocorreu um erro ao processar sua requisição.")

async def partidas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        partidas = listar_proximas_partidas()
        resposta = formatar_partidas(partidas)
        await update.message.reply_text(
            resposta, 
            parse_mode='Markdown', 
            disable_web_page_preview=False
        )
    except Exception as e:
        print(f"Erro: {e}")
        await update.message.reply_text("⚠️ Erro ao buscar partidas.")

async def historico(update: Update, context: ContextTypes.DEFAULT_TYPE):
    limit = int(context.args[0]) if context.args else 5
    partidas = buscar_historico(limit)
    await update.message.reply_text(formatar_historico(partidas), parse_mode='Markdown')


def main():

    
    print("🔄 Iniciando o Pantera News...")    
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("jogadores", jogadores))
    app.add_handler(CommandHandler("campeonatos", campeonatos))
    app.add_handler(CommandHandler("ranking", ranking))
    app.add_handler(CommandHandler("estatisticas", estatisticas))
    app.add_handler(CommandHandler("partidas", partidas))
    app.add_handler(CommandHandler("historico", historico))
    app.add_handler(CommandHandler("historia", historia))

    print_banner()
    

    app.run_polling()

if __name__ == "__main__":
    main()
try:   
        threading.Thread(target=lambda: asyncio.run(keep_alive()), daemon=True).start()
        
        PORT = int(os.environ.get('PORT', 5000))
        application.run(port=PORT)
except Exception as e:
        print(f"Erro crítico: {e}")

