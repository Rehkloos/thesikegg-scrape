from bs4 import BeautifulSoup
from flask import Flask, render_template, current_app, jsonify
from flask_cors import CORS
import json
import requests

app = Flask(__name__, template_folder='frontpage')
CORS(app)


def spike():
  URL = 'https://www.thespike.gg'
  html = requests.get(URL).text
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


@app.route('/')
def root():
    return render_template('index.html')


@app.route("/latest_news")
def spike_news():
  return current_app.response_class(json.dumps(spike(), indent=4), mimetype="application/json")


if __name__ == "__main__":
  app.run(
      host="0.0.0.0",
      port=9271
  )
