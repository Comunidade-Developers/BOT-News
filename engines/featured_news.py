import httpx
from bs4 import BeautifulSoup


async def get_featured_news():

  news = []
  async with httpx.AsyncClient() as client:
    response = await client.get('https://news.google.com/showcase?hl=pt-BR&gl=BR&ceid=BR%3Apt-419')
    soup = BeautifulSoup(response.text, 'html.parser')
    cells = soup.find_all('div', class_='LpIL4e MgSxke')
    for cell in cells:
      newspaper = cell.find('img', class_='UiDffd b1F67d').get('alt')
      title = cell.find('div', class_='JrYg1b vP0hTc').get_text()
      subtitle = cell.find('a', class_='kEAYTc r5Cqre').get_text()
      url = cell.find('a', class_='kEAYTc r5Cqre')['href']
      time = cell.find('time', class_='xsHp8').get_text()
      link = f'https://news.google.com{url}'

      new = [newspaper, title, subtitle, time, link]
      news.append(new)

  return