from app import chatbot
from chatterbot.trainers import ListTrainer
import pandas as pd

df = pd.read_csv("question and answer pairs.csv")
trainer = ListTrainer(chatbot)

for _, row in df.iterrows():
    trainer.train([row["Question"], row["Sentence"]])


r = chatbot.get_response("How are you")
