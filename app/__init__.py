from flask import Flask 
from jinja2 import StrictUndefined
from chatterbot import Chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
bot = Chatbot()


@app.route("/")
def home():
    return "welcome"