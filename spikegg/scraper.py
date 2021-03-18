from bs4 import BeautifulSoup
import requests
import re


def spike():
  headers = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Max-Age': '3600',
      'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
  }
  URL = 'https://www.thespike.gg'
  html = requests.get(URL, headers=headers).text
  soup = BeautifulSoup(html, 'html.parser')
  if soup.find(class_="home-news-area") == None:
    return None
  else:
    spike_element = soup.find(
        'ul', attrs={"class": "item-list"}).parent.find_all('li', attrs={"class": "item element-trim-button"})
    spike = []
    for spikes in spike_element:
        inner = spikes.find('div', attrs={"class": "inner"})
        title = inner.find('div', attrs={"class": "news-title"})
        title = title.text.strip()
        url = spikes.find('a').attrs['href']
        url = f"https://www.thespike.gg{url}"
        date = inner.find('div', attrs={"class": "news-info"})
        date = date.find(attrs={"class": "date"})
        date = date.text.strip()

        spike.append({
            "title": title,
            "url": url,
            "date": date
        })

        segments = {"segments": spike}

        data = {"data": segments}

    return data
