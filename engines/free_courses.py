import httpx
from bs4 import BeautifulSoup

async def get_free_courses():

  news = []
  async with httpx.AsyncClient() as client: 
    response = await client.get('https://news.google.com/search?q=cursos%20gratuitos%20de%20tecnologia&hl=pt-BR&gl=BR&ceid=BR%3Apt-419')
    soup = BeautifulSoup(response.text, 'html.parser')
    cells = soup.find_all('c-wiz', class_='PO9Zff Ccj79 kUVvS')
    for cell in cells:
      title = cell.find('a', class_='JtKRv').get_text()
      url = cell.find('a', class_='JtKRv')['href']
      company = cell.find('div', class_='vr1PYe').get_text()
      link = f'https://news.google.com{url}'

      new = [title, company, link]

      news.append(new)

  return news  
  

