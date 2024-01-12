import http.client
import json
from datetime import datetime, timedelta


def get_dates():
    current_date = datetime.now()
    two_days_ago = current_date - timedelta(days=2)
    return two_days_ago.strftime('%d/%m/%Y'), current_date.strftime('%d/%m/%Y')


async def esports():
    conn = http.client.HTTPSConnection("newsnow.p.rapidapi.com")

    from_date, to_date = get_dates()

    payload = f'''{{
        "query": "sports",
        "page": 1,
        "time_bounded": true,
        "from_date": "{from_date}",
        "to_date": "{to_date}",
        "location": "brazil",
        "category": "",
        "source": ""
    }}'''

    headers = {
        'content-type': "application/json",
        'X-RapidAPI-Key': "05bb657f29mshb6eec31086f745cp106d91jsnee2984f02610",
        'X-RapidAPI-Host': "newsnow.p.rapidapi.com"
    }

    conn.request("POST", "/newsv2", payload, headers)

    res = conn.getresponse()
    data = res.read()

    news_data = json.loads(data.decode("utf-8"))
    news = []
    for news_item in news_data.get('news', []):
        title = news_item.get('title')
        date = news_item.get('date')
        link = news_item.get('url')
        source = news_item.get('source')
        news.append((title, date, link, source))

    return news
