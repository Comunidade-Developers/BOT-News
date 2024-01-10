import asyncio
import keyring
import hikari
from hikari import intents
from engines.techonology import technology
from engines.esports import esports

channel_technology = keyring.get_password('bot_news', 'channel_technology')
channel_esports = keyring.get_password('bot_news', 'channel_e-sports')
sent_news = []

bot = hikari.GatewayBot(keyring.get_password('bot_news', 'token'), intents=intents.Intents.ALL)

@bot.listen()
async def on_started(event: hikari.StartedEvent) -> None:
    while True:
        results = await technology()
        for result in results:
            if result[0] not in sent_news:
                sent_news.append(result[0])
                news_info = f'{"-"*50}\nTÍTULO DA NOTICIA: {result[0]}\nDATA: {result[1]}\nLINK: {result[2]}\nEMPRESA: {result[3]}'
                await bot.rest.create_message(channel_technology, news_info)
                await asyncio.sleep(30)

        results = await esports()
        for result in results:
            if result[0] not in sent_news:
                sent_news.append(result[0])
                news_info = f'{"-"*50}\nTÍTULO DA NOTICIA: {result[0]}\nDATA: {result[1]}\nLINK: {result[2]}\nEMPRESA: {result[3]}'
                await bot.rest.create_message(channel_esports, news_info)
                await asyncio.sleep(30)

        await asyncio.sleep(86400)

bot.run()
