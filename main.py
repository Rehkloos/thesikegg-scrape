from flask import Flask, render_template, current_app, jsonify
from flask_cors import CORS
from flask_caching import Cache
from api.scrape import Spike
import json

app = Flask(__name__, template_folder='frontpage')
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
CORS(app)
spike = Spike()


@cache.cached(timeout=300)
@app.route('/', methods=['GET'])
def root():
  return render_template('index.html')

@cache.cached(timeout=300)
@app.route("/latest_news", methods=['GET'])
def spike_news():
  return current_app.response_class(json.dumps(spike.get_news(), indent=4), mimetype="application/json")

@cache.cached(timeout=300)
@app.route('/matches/results', methods=['GET'])
def results():
    return current_app.response_class(json.dumps(spike.get_match_results(), indent=4), mimetype="application/json")

@cache.cached(timeout=300)
@app.route('/rankings', methods=['GET'])
def rankings():
    return current_app.response_class(json.dumps(spike.get_rankings(), indent=4), mimetype="application/json")



if __name__ == "__main__":
      app.run(
      host="0.0.0.0"
  )
