import time
import telebot
from config import BOT_TOKEN
from tools.imdb import scrapeimdb

bot = telebot.TeleBot(BOT_TOKEN)
PARSE_MODE = "Markdown"

import logging

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

@bot.message_handler(['start'])
def start(message):
    bot_name = bot.get_me().first_name
    user_name = message.from_user.first_name if message.from_user.first_name else "User"
    bot.reply_to(message,f"Hello, {user_name}! \n\nThis is {bot_name}. I will help you find out information about movies. /help for further more.", parse_mode=PARSE_MODE)

@bot.message_handler(['help'])
def start(message):
    bot.reply_to(message,"Just send me any movie/series name and wait a moment before I send you details.", parse_mode=PARSE_MODE)

@bot.message_handler()
def handle_message(message):
    try:
        start_time = time.time()
        query = message.text.lower()
        data, poster_url = scrapeimdb(query)
        end_time = time.time()
        elapsed_time = end_time - start_time
        bot.send_photo(message.chat.id, photo=poster_url, caption=f"{data}\n\n `took: {elapsed_time:.2f} sec`", parse_mode=PARSE_MODE)
    except Exception as e:
        print(e)
        bot.reply_to(message, f"*Title*: `{query}`\n*Result*: `Not found.`", parse_mode=PARSE_MODE) 



bot.polling()