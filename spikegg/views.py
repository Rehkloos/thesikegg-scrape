from flask import Flask, render_template, current_app, jsonify
import json

from spikegg import app
from spikegg.scraper import spike


@app.route('/')
def root():
    return render_template('index.html')


@app.route("/latest_news")
def spike_news():
  return current_app.response_class(json.dumps(spike(), indent=4), mimetype="application/json")
