import telebot
import os
from dotenv import load_dotenv
from datetime import datetime
from datetime import date
load_dotenv()
token = 'enter your bot token'
bot = telebot.TeleBot(token)
i="0"
type_input=" "
#commands ->
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
@bot.message_handler(['start'])
def start(massage):
    type_input=" "
    print("requested...")
    bot_name = bot.get_me().first_name
    user_name = massage.from_user.first_name 
    user_last_name = massage.from_user.last_name 
    bot.send_message(massage.chat.id,"""hello my friend """ +user_name+" "+user_last_name+ """ .
how are you??
I am IMDBFM bot . To help enter "/help ".To know about me enter "/about".""")
    print("delivered...")
@bot.message_handler(['exit'])
def exit(massage):
    global type_input
    print("requested...")
    bot.send_message(massage.chat.id,"You successfully exited. For restart /start")
    type_input=" "
    print("delivered...")
@bot.message_handler(['help'])
def help(massage):
    print("requested...")
    bot.send_message(massage.chat.id,"""for movies - m
for web series - s
for Time - /time
for Date - /date
for dat - /day
for know about me - /about""")
    print("delivered...")
@bot.message_handler(['reset'])
def reset(massage):
    print("requested...")
    bot.send_message(massage.chat.id,"""for movies - m
for web series - s""")
    print("delivered...")
@bot.message_handler(['again'])
def reset(massage):
    bot.send_message(massage.chat.id,"Go on!!!")
@bot.message_handler(['time'])
def time(massage):
    current_time1 = datetime.now()
    current_time2 = current_time1.strftime("%I:%M %p")
    print("requested...")
    bot.reply_to(massage,current_time2)
    print("delivered...")
@bot.message_handler(['date'])
def date(massage):
    todays_date=datetime.today().date()
    print("requested...")
    bot.reply_to(massage,todays_date)
    print("delivered...")
@bot.message_handler(['day'])
def day(massage):
    current_time = datetime.now()
    todays_date2=current_time.strftime("%A")
    print("requested...")
    bot.reply_to(massage,todays_date2)
    print("delivered...")
@bot.message_handler(['about'])
def about(massage):
    print("requested...")
    bot.send_message(massage.chat.id,"""Hello. Iam IMDBFM a telegram bot.
My job is to show you the IMDB rating of any movie and if there is any free source of that movie, share the link with you.
Besides, You can know many things from me.
like : 
        1.Time "/time" 
        2.Date "/date" 
        3.Day "/day"
        4.Help "/help"
        """)
    print("delivered...")
@bot.message_handler()
def handle_message(massage):
    #type ->
    #\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
    global i, type_input
    i="0"
    if massage.text.lower() == "m":
        i="1"
        type_input="m"
        print("requested...")
        bot.reply_to(massage,"enter your movie name.")
        print("delivered...")
    elif massage.text.lower() == "s":
        i="1"
        type_input="s"
        print("requested...")
        bot.reply_to(massage,"enter your web series name.")
        print("delivered...")
    #chat_gpt_work
    #\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
    if massage.text.lower() == "hello" and type_input==" " or massage.text.lower() == "hi" and type_input==" " or massage.text.lower() == "hello imdbfm" and type_input==" " or massage.text.lower() == "hi imdbfm" and type_input==" ":
        i="1"
        print("requested...")
        bot.reply_to(massage,"Hi.How can i help you? /start")                       
        print("delivered...")
    if massage.text.lower() == "what is your name" and type_input==" " or massage.text.lower() == "what is your name?" and type_input==" " or massage.text.lower() == "who are you" and type_input==" " or massage.text.lower() == "who are you?" and type_input==" ":
        i="1"
        print("requested...")
        bot.reply_to(massage,"Hello. Iam IMDBFM.The Rayhan PY made me.")
        print("delivered...")
    if massage.text.lower() == "tell me about you" and type_input==" " or massage.text.lower() == "tell me about you." and type_input==" " or massage.text.lower() == "tell me something about you." and type_input==" " or massage.text.lower() == "tell me something about you" and type_input==" " or massage.text.lower() == "what can you do" and type_input==" " or massage.text.lower() == "what can you do?" and type_input==" ":
        i="1"
        print("requested...")
        bot.reply_to(massage,"""Hello. Iam IMDBFM a telegram bot.
My job is to show you the IMDB rating of any movie and if there is any free source of that movie, share the link with you.
Besides, You can know many things from me.
like : 
        1. Time "/time" 
        2. Date "/date" 
        3. Day "/day"
        4. help "/help"
        """)
        print("delivered...")
    #movei ->
    #\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
    elif massage.text.lower() =="mr9" and type_input=="m":
        i="1"
        print("requested...")
        bot.reply_to(massage,"go to the link -> https://www.imdb.com/title/tt9044418/")
        bot.reply_to(massage,"we do not have any free link of MR9 .. we are really sorry..")
        print("delivered...")
        bot.reply_to(massage,"To search Again - /again")
    elif massage.text.lower() =="dunki" and type_input=="m":
        i="1"
        print("requested...")
        bot.reply_to(massage,"go to the link -> https://www.imdb.com/title/tt15428134/")
        bot.reply_to(massage,"we do not have any free link of Dunki .. we are really sorry..")
        print("delivered...")
        bot.reply_to(massage,"To search Again - /again")
    elif massage.text.lower() =="pathaan" and type_input=="m":
        i="1"
        print("requested...")
        bot.reply_to(massage,"go to the link -> https://www.imdb.com/title/tt12844910/")
        bot.reply_to(massage,"go to there for the free movei link -> https://www.youtube.com/watch?v=LRmbq19xDZM")
        print("delivered...")
        bot.reply_to(massage,"To search Again - /again")
    elif massage.text.lower() =="jawan" and type_input=="m":
        i="1"
        print("requested...")
        bot.reply_to(massage,"go to the link -> https://www.imdb.com/title/tt15354916/")
        bot.reply_to(massage,"go to there for the free movei link -> https://www.youtube.com/watch?v=2wLTkQVdOYw")
    #web seise ->
    #\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
    elif massage.text.lower() =="money heist 1" and type_input=="s":
        i="1"
        print("requested...")
        bot.reply_to(massage,"go to the link -> https://www.imdb.com/title/tt6468322/")
        bot.reply_to(massage,"go to there for the free movei link -> https://ww8.soap2dayhd.co/film/money-heist-season-1-29008/")
        print("delivered...")
        bot.reply_to(massage,"To search Again - /again")
    elif massage.text.lower() =="money heist 2" and type_input=="s":
        i="1"
        print("requested...")
        bot.reply_to(massage,"go to the link -> https://www.imdb.com/title/tt6468322/")
        bot.reply_to(massage,"go to there for the free movei link -> https://sdmoviespoint.fan/money-heist-season-2-full-hd-free-download-720p/")
        print("delivered...")
        bot.reply_to(massage,"To search Again - /again")
    elif massage.text.lower() =="money heist 3" and type_input=="s":
        i="1"
        print("requested...")
        bot.reply_to(massage,"go to the link -> https://www.imdb.com/title/tt6468322/")
        bot.reply_to(massage,"go to there for the free movei link -> https://taurenidushq.blogspot.com/2021/02/download-money-heist-season-3-hindi-dubbed.html")
        print("delivered...")
        bot.reply_to(massage,"To search Again - /again")
    elif massage.text.lower() =="money heist 4" and type_input=="s":
        i="1"
        print("requested...")
        bot.reply_to(massage,"go to the link -> https://www.imdb.com/title/tt6468322/")
        bot.reply_to(massage,"go to there for the free movei link -> https://sdmoviespoint.fan/money-heist-season-4-full-hd-free-download-720p/")
        print("delivered...")
        bot.reply_to(massage,"To search Again - /again")
    elif massage.text.lower() =="money heist 5" and type_input=="s":
        i="1"
        print("requested...")
        bot.reply_to(massage,"go to the link -> https://www.imdb.com/title/tt6468322/")
        bot.reply_to(massage,"go to there for the free movei link -> https://ww8.soap2dayhd.co/film/money-heist-season-5-1627222840/")
        print("delivered...")
        bot.reply_to(massage,"To search Again - /again")
    #unexpected error ->
    #\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
        
    if i!="1":
        print("requested...")
        bot.reply_to(massage,"""opss!! chack your searching type or we donot have this movei / web seise .
To reset type "/reset".
                     
we have movei / web seise like : 
1. MR9
2. Dunki
3. Jawan
4. Pathaan
5. Money heist 1/2/3/4/5
                     
for exit - /exit
""")

        print("delivered...")
    
bot.polling()
