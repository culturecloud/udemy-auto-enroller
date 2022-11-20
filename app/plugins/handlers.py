import requests
from pyrogram import Client, filters

@Client.on_message(filters.chat('TestingChannel404'))
def link_parser(_, msg):
    button = list(msg.reply_markup.inline_keyboard)
    coursedb_link = button[0][0].url
    udemy_link = (requests.get(coursedb_link)).url
    print(udemy_link)
    