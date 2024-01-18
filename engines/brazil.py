import httpx
from bs4 import BeautifulSoup

async def get_brazil():

  news = []

  async with httpx.AsyncClient() as client:
    response = await client.get('https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNREUxWm5JU0JYQjBMVUpTS0FBUAE?hl=pt-BR&gl=BR&ceid=BR%3Apt-419')
    soup = BeautifulSoup(response.text, 'html.parser')
    cells = soup.find_all('div', class_='W8yrY')
    for cell in cells:
      url_article = cell.find('a', class_='WwrzSb')['href']
      link_article = f'https://news.google.com{url_article}'
      title_article = cell.find('a', class_='gPFEn').get_text()
      company_article = cell.find('div', class_='vr1PYe').get_text()

      cells = soup.find_all('article', class_='UwIKyb')
      for cell in cells:
        url = cell.find('a', class_='gPFEn')['href']
        link = f'https://news.google.com{url}'
        title = cell.find('a', class_='gPFEn').get_text()
        company = cell.find('div', class_='vr1PYe').get_text()

        new = [title_article,company_article,link_article,title, company, link]
        news.append(new)

  return
