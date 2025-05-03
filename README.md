# 🐆 Pantera News — Bot do time de CS2 DA FURIA

**Pantera News** é um bot Telegram desenvolvido para acompanhar em tempo real os jogos da FURIA Esports no CS2. O bot oferece estatísticas, agenda de partidas, histórico da organização, etc.

## 🎯 Funcionalidades

* 🔹 Comando `/historia`: Resumo completo da trajetória da FURIA Esports.
* 🔹 Comando `/estatisticas`: Exibe estatísticas detalhadas dos jogadores.
* 🔹 Comando `/ranking`: Mostra a posição da FURIA nos rankings atuais.
* 🔹 Comando `/historico`, `campeonatos`, `/estatisticas`: Informações específicas de desempenho.
* 🔹 Comando `/partidas`: Informações sobre as proximas partidas da Furia.
* 🔹 Atualização automática dos dados diretamente no banco de dados SQLite.
* 🔹 Estrutura preparada para futura integração com APIs de esports (ex: HLTV).

## 🗂 Estrutura do Projeto

```
Pantera News/
├── Atualizar dados/
│   ├── atualizar_estatisticas.py
│   ├── atualizar_funcao.py
│   └── ...
├── commands/
│   ├── campeonatos.py
│   ├── estatisticas.py
│   ├── historico.py
│   ├── ...
├── Verificar tabelas/
├── dados.py
├── database.sqlite
├── furiadb.py
├── panterabot.py
├── requirements.txt
└── .env
```

## ⚙️ Instalação e Execução Local

1. Clone o repositório:

   ```bash
   git clone https://github.com/seuusuario/pantera-news.git
   cd pantera-news
   ```

2. Crie o arquivo `.env` com as variáveis de ambiente:

   ```env
   TELEGRAM_TOKEN=seu_token_do_bot_aqui
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute o bot:

   ```bash
   python panterabot.py
   ```

## ☁️ Deploy no Railway

1. Crie uma conta ou acesse o [Railway](https://railway.app/).
2. Crie um novo projeto e conecte seu repositório GitHub.
3. Adicione a variável de ambiente `TELEGRAM_TOKEN` na aba "Variables".
4. Configure o comando de inicialização:

   ```bash
   python panterabot.py
   ```
5. O Railway cuidará do deploy contínuo do bot.

## 📋 Requisitos

* Python 3.10+
* SQLite (utilizado localmente)
* `python-telegram-bot`
* `python-dotenv`, `requests` etc.

## 🤝 Contribuição

Contribuições são bem-vindas! Abra uma issue ou envie um pull request com sugestões de melhorias ou correções.

## 📄 Licença

Este projeto está licenciado sob a licença MIT.
