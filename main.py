import discord
import httpx
from bs4 import BeautifulSoup

client = discord.Client()


async def buscar_noticias():
    url = 'https://www.google.com/search?q=noticias&hl=pt-BR&gl=BR&ceid=BR:pt-419&source=lnms&tbm=nws'
    headers = {'User-Agent': 'Mozilla/5.0'}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    noticias = soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd')

    noticias_texto = [noticia.get_text() for noticia in noticias]
    return '\n'.join(noticias_texto)


@client.event
async def on_ready():
    print(f'Conectado como {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$noticias'):
        await message.channel.send('Buscando notícias...')
        noticias = await buscar_noticias()
        await message.channel.send(noticias)

client.run('token')
