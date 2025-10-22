from flask import Flask 
from jinja2 import StrictUndefined
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd


app = Flask(__name__)
chatbot = ChatBot("Bot 1")
