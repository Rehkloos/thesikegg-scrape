import spikegg.views
from flask import Flask
from flask_cors import CORS

app = Flask(__name__, template_folder='frontpage')
CORS(app)
