import requests

url = "https://newsnow.p.rapidapi.com/newsv2"

payload = {
	"query": "news",
	"page": 1,
	"time_bounded": True,
	"from_date": "18/12/2023",
	"to_date": "25/12/2023",
	"location": "",
	"category": "",
	"source": ""
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "b7c205fb69mshd249a9ea595055dp14caf6jsn47e78ac78f26",
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
