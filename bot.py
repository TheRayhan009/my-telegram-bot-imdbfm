import telebot
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("TOKEN")
bot = telebot.TeleBot(token)
i=0
user_name="@rayhan_py"
@bot.message_handler(['start'])
def start(massage):
    print("recuestde...")
    bot.reply_to(massage,"""hello my friend """ +user_name+ """ .how are you?? i am imdbfm bot . to help enter "/help ".""")
    print("delivard..")
@bot.message_handler(['help'])
def start(massage):
    print("recuestde...")
    bot.reply_to(massage,"""for movies - m
for web series - s""")
    print("delivard..")
@bot.message_handler()
def handle_message(massage):
    if massage.text.lower() == "m":
        i=1
        print("recuestde...")
        bot.reply_to(massage,"enter your movie name.")
        print("delivard..")
    elif massage.text.lower() == "s":
        i=1
        print("recuestde...")
        bot.reply_to(massage,"enter your web series name.")
        print("delivard..")
    elif massage.text.lower() =="mr9":
        i=1
        print("recuestde...")
        bot.reply_to(massage,"go to the link -> https://www.imdb.com/title/tt9044418/")
        bot.reply_to(massage,"we do not have any free link of MR9 .. we are really sorry..")
        print("delivard..")
    elif massage.text.lower() =="dunki":
        i=1
        print("recuestde...")
        bot.reply_to(massage,"go to the link -> https://www.imdb.com/title/tt15428134/")
        bot.reply_to(massage,"we do not have any free link of Dunki .. we are really sorry..")
        print("delivard..")
    elif massage.text.lower() =="pathaan":
        i=1
        print("recuestde...")
        bot.reply_to(massage,"go to the link -> https://www.imdb.com/title/tt12844910/")
        bot.reply_to(massage,"go to there for the free movei link -> https://www.youtube.com/watch?v=LRmbq19xDZM")
        print("delivard..")
    elif massage.text.lower() =="jawan":
        i=1
        print("recuestde...")
        bot.reply_to(massage,"go to the link -> https://www.imdb.com/title/tt15354916/")
        bot.reply_to(massage,"go to there for the free movei link -> https://www.youtube.com/watch?v=2wLTkQVdOYw")

        print("delivard..")
    else:
        i=0
    if i==0:
        print("recuestde...")
        bot.reply_to(massage,"opss!!")
        print("delivard..")



bot.polling()