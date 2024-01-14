import keyring
import hikari
from hikari import intents
import asyncio

from engines.technology import get_technology
from engines.esports import get_esports
from engines.free_courses import get_free_courses
from engines.sports import get_sports
from engines.brazil import get_brazil
from engines.world import get_world
from engines.featured_news import get_featured_news

token = keyring.get_password('bot_vagas', 'token')

channel_technology = keyring.get_password('bot_news', 'channel_technology')
channel_esports = keyring.get_password('bot_news', 'channel_e-sports')
channel_free_courses = keyring.get_password('bot_news', 'channel_free_courses')
channel_sports = keyring.get_password('bot_news', 'channel_sports')
channel_brazil = keyring.get_password('bot_news', 'channel_brazil')
channel_world = keyring.get_password('bot_news', 'channel_world')
channel_featured_news = keyring.get_password('bot_news', 'channel_featured_news')

bot = hikari.GatewayBot(keyring.get_password('bot_news', 'token'), intents=intents.Intents.ALL)

sent_news = []

@bot.listen()
async def on_started(event: hikari.StartedEvent) -> None:
    while True:
        results = await get_technology()
        for result in results:
            if result[0] not in sent_news:
                sent_news.append(result[0])
                news_info = f'{"-"*20}\nTÍTULO DA NOTICIA: {result[0]}\nJORNAL: {result[1]}\nLINK: {result[2]}\n'
                await bot.rest.create_message(channel_technology, news_info)
                await asyncio.sleep(2)
            await asyncio.sleep(2)

        results = await get_esports()
        for result in results:
            if result[0] not in sent_news:
                sent_news.append(result[0])
                news_info = f'{"-"*20}\nTÍTULO DA NOTICIA: {result[0]}\nJORNAL: {result[1]}\nLINK: {result[2]}\n'
                await bot.rest.create_message(channel_esports, news_info)
                await asyncio.sleep(2)
            await asyncio.sleep(2)

        results = await get_free_courses()
        for result in results:
            if result[0] not in sent_news:
                sent_news.append(result[0])
                news_info = f'{"-"*20}\nTÍTULO DA NOTICIA: {result[0]}\nEMPRESA: {result[1]}\nLINK: {result[2]}\n'
                await bot.rest.create_message(channel_free_courses, news_info)
                await asyncio.sleep(2)
            await asyncio.sleep(2)

        results = await get_sports()
        for result in results:
            if result[0] not in sent_news:
                sent_news.append(result[0])
                news_info = f'{"-"*20}\nTÍTULO DA NOTICIA: {result[0]}\nEMPRESA: {result[1]}\nLINK: {result[2]}\nTÍTULO DA NOTICIA: {result[3]}\nEMPRESA: {result[4]}\nLINK: {result[2]}\n'
                await bot.rest.create_message(channel_sports, news_info)
                await asyncio.sleep(2)
            await asyncio.sleep(2)

        results = await get_brazil()
        for result in results:
            if result[0] not in sent_news:
                sent_news.append(result[0])
                news_info = f'{"-"*20}\nTÍTULO DA NOTICIA: {result[0]}\nEMPRESA: {result[1]}\nLINK: {result[2]}\nTÍTULO DA NOTICIA: {result[3]}\nEMPRESA: {result[4]}\nLINK: {result[2]}\n'
                await bot.rest.create_message(channel_brazil, news_info)
                await asyncio.sleep(2)
            await asyncio.sleep(2)
        
        results = await get_world()
        for result in results:
            if result[0] not in sent_news:
                sent_news.append(result[0])
                news_info = f'{"-"*20}\nTÍTULO DA NOTICIA: {result[0]}\nEMPRESA: {result[1]}\nLINK: {result[2]}\nTÍTULO DA NOTICIA: {result[3]}\nEMPRESA: {result[4]}\nLINK: {result[2]}\n'
                await bot.rest.create_message(channel_world, news_info)
                await asyncio.sleep(2)
            await asyncio.sleep(2)

        results = await get_featured_news()
        for result in results:
            if result[0] not in sent_news:
                sent_news.append(result[0])
                news_info = f'{"-"*20}\nTÍTULO DA NOTICIA: {result[0]}\nEMPRESA: {result[1]}\nLINK: {result[2]}\nTÍTULO DA NOTICIA: {result[3]}\nEMPRESA: {result[4]}\nLINK: {result[2]}\n'
                await bot.rest.create_message(channel_featured_news, news_info)
                await asyncio.sleep(2)
            await asyncio.sleep(43200)
bot.run()
