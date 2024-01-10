import requests

url = "https://newsnow.p.rapidapi.com/newsv2"

payload = {
	"query": "AI",
	"page": 1,
	"time_bounded": True,
	"from_date": "01/02/2021",
	"to_date": "05/06/2021",
	"location": "",
	"category": "",
	"source": ""
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "newsnow.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()

for news_item in data.get('news', []):
  title = news_item.get('title')
  date = news_item.get('date')
  link = news_item.get('url')
  source = news_item.get('source')

  print('-'*50)
  print(title)
  print(date)
  print(link)
  print(source)
  print('-'*50)
