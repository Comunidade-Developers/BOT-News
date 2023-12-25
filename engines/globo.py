import requests
from bs4 import BeautifulSoup


def buscar_noticias():

  url = 'https://www.techtudo.com.br/mobile/'

  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  cells = soup.find_all('div', class_='feed-post-body')
  for cell in cells:
    title = cell.find('h2', class_='feed-post-link gui-color-primary gui-color-hover').get_text()
    print(title)


buscar_noticias()