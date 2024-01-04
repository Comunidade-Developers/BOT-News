import httpx
from datetime import datetime, timedelta
import schedule
import time
import asyncio


async def get_news() -> list:
    news = []
    url = "https://newsnow.p.rapidapi.com/newsv2"
    current_date = datetime.now()
    three_days_ago = current_date - timedelta(days=3)

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "b7c205fb69mshd249a9ea595055dp14caf6jsn47e78ac78f26",
        "X-RapidAPI-Host": "newsnow.p.rapidapi.com"
    }

    payload = {
        "query": "business",
        "page": 1,
        "time_bounded": True,
        "from_date": three_days_ago.strftime("%d/%m/%Y"),
        "to_date": current_date.strftime("%d/%m/%Y"),
        "location": "",
        "category": "",
        "source": ""
    }

    async with httpx.AsyncClient() as client:  # Increase timeout
      response = await client.post(url, json=payload, headers=headers)

      if response.status_code == 200:
        data = response.json()

        for news_item in data.get('news', []):
          title = news_item.get('title')
          date = news_item.get('date')
          link = news_item.get('url')
          source = news_item.get('source')

          new = [title, date, link, source]
          news.append(new)

    return news

def job():
    news = asyncio.run(get_news())
    print(news)

# Agende o trabalho para ser executado todos os dias
schedule.every(2).days.at("00:00").do(job)

while True:
    # Executa tarefas pendentes
    schedule.run_pending()
    time.sleep(1)
