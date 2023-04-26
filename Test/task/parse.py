import requests
from bs4 import BeautifulSoup


def get_href() -> list:
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    }
    url = 'https://news.google.com/home?hl=ru&gl=RU&ceid=RU%3Aru'

    responce = requests.get(url=url, headers=headers).text

    soup = BeautifulSoup(responce, 'lxml')
    res = soup.find_all('a', 'WwrzSb')
    news_list = []

    for item in res:
        news_list.append('https://news.google.com' + str(item.get('href'))[1:])

    return news_list


news_list = ['https://news.google.com/articles/CBMibmh0dHBzOi8vd3d3LnJ6bi5pbmZvL25ld3MvMjAyMy80LzI0L3YtcG9kbW9za292ZS11cGFsLWRyb24ta2FtaWthZHplLXMtMTcta2lsb2dyYW1tYW1pLXZ6cnl2Y2hhdGtpLTI2NzU1MC5odG1s0gEA?hl=ru&gl=RU&ceid=RU%3Aru',
             'https://news.google.com/articles/CBMiIGh0dHBzOi8vdXJhLm5ld3MvbmV3cy8xMDUyNjQzNjE00gEkaHR0cHM6Ly9hbXAudXJhLm5ld3MvbmV3cy8xMDUyNjQzNjE0?hl=ru&gl=RU&ceid=RU%3Aru', '/articles/CBMiLGh0dHBzOi8vd3d3LmZvbnRhbmthLnJ1LzIwMjMvMDQvMjQvNzIyNDUxNzEv0gEA?hl=ru&gl=RU&ceid=RU%3Aru',
             'https://news.google.com/articles/CBMiGWh0dHBzOi8vbGlmZS5ydS9wLzE1NzQ1ODTSAR1odHRwczovL2xpZmUucnUvcC8xNTc0NTg0L2FtcA?hl=ru&gl=RU&ceid=RU%3Aru',
             'https://news.google.com/articles/CBMiJWh0dHBzOi8vd3d3LmtvbW1lcnNhbnQucnUvZG9jLzU5NTI4NjnSASVodHRwczovL3d3dy5rb21tZXJzYW50LnJ1L2FtcC81OTUyODY5?hl=ru&gl=RU&ceid=RU%3Aru',
             'https://news.google.com/articles/CBMidWh0dHBzOi8vd3d3LnZlZG9tb3N0aS5ydS9maW5hbmNlL2FydGljbGVzLzIwMjMvMDQvMjQvOTcyMjg0LXRzYi1yYXpyYWJvdGFsLXN0YW5kYXJ0LWRseWEtcmVzaGVuaXlhLXByb2JsZW0tZG9semhuaWtvdtIBAA?hl=ru&gl=RU&ceid=RU%3Aru',
             'https://news.google.com/articles/CBMiJ2h0dHBzOi8vd3d3LmludGVyZmF4LnJ1L2J1c2luZXNzLzg5NzQ1OdIBImh0dHBzOi8vd3d3LmludGVyZmF4LnJ1L2FtcC84OTc0NTk?hl=ru&gl=RU&ceid=RU%3Aru',
             'https://news.google.com/articles/CBMicWh0dHBzOi8vd3d3LmZvcmJlcy5ydS9maW5hbnN5LzQ4ODI3My1jYi1wcmVkbG96aWwtYmFua2FtLWRvZ292YXJpdmF0LXNhLW8tdnp5c2thbmlpLWRvbGdvdi1zLXByb2JsZW1ueWgtemFlbXNpa2920gEA?hl=ru&gl=RU&ceid=RU%3Aru',
             'https://news.google.com/articles/CBMiwwFodHRwczovL21lZHV6YS5pby9uZXdzLzIwMjMvMDQvMjQvdGhlLXdhc2hpbmd0b24tcG9zdC11a3JhaW5za2F5YS1yYXp2ZWRrYS1zb2JpcmFsYXMtdi1nb2RvdnNjaGludS1uYWNoYWxhLXJvc3NpeXNrb2dvLXZ0b3J6aGVuaXlhLW5hbmVzdGktdWRhcnktcG8tdGVycml0b3JpaS1yZi1uby1wb21lbnlhbGEtcGxhbnktcG8tcHJvc2JlLXNzaGHSAccBaHR0cHM6Ly9tZWR1emEuaW8vYW1wL25ld3MvMjAyMy8wNC8yNC90aGUtd2FzaGluZ3Rvbi1wb3N0LXVrcmFpbnNrYXlhLXJhenZlZGthLXNvYmlyYWxhcy12LWdvZG92c2NoaW51LW5hY2hhbGEtcm9zc2l5c2tvZ28tdnRvcnpoZW5peWEtbmFuZXN0aS11ZGFyeS1wby10ZXJyaXRvcmlpLXJmLW5vLXBvbWVueWFsYS1wbGFueS1wby1wcm9zYmUtc3NoYQ?hl=ru&gl=RU&ceid=RU%3Aru',
             'https://news.google.com/articles/CBMiLmh0dHBzOi8vbmV3cy5wbi9ydS9SdXNzaWFJbnZhZGVkVWtyYWluZS8yODk4NjHSAQA?hl=ru&gl=RU&ceid=RU%3Aru'
]
