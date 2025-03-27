import telebot
from telebot.types import Message
import time

bot = telebot.TeleBot("7838586771:AAHX5wvomXJC0K7E3ZfSOp17vrHqp3Zbp8M")


@bot.message_handler(commands=["ecology"])
def whatseclology(message:Message):
    bot.send_message(message.chat.id,f"what peopels make with ecology?\npeoples in the world make fastest pollution with ecology after creating technologies")


@bot.message_handler(commands=["reasons"])
def reasonsofpe(message:Message):
    bot.send_message(message.chat.id,f"""
reasons of ecology pollutions:
1.creating technologies, after creating technologies the pollutions of ecology increased because                     
technologies work with electronic and electronik work with burning wood(and more m) and burning makes co2(carbon dioxide) and he don't leave of the planet 
people can't breathe co2(carbon dioxide).

2.using cars, after making cars the pollutions of ecology increased because
to use cars we burning gasoline and burning makes co2(carbon dioxide).
                     
3.garbage, the peoples thorow the garbage in the world and dont make with him(world try to make with garbage new items) and
his destroy ecology
""")


@bot.message_handler(commands=["WhatToDo"])
def WTD(message:Message):
    bot.send_message(message.chat.id, f"""what you can to do for save ecology:
1) you can use transport without gasoline or use electronik cars

2) you can smaller the time from phones, pc, and more electronik""")
    

@bot.message_handler(commands=["facts"])
def facts(message:Message):
    bot.send_message(message.chat.id, f"""facts on ecology:
1) one big tree can to give O (oxygen) for 10 peoples

2) 1 plastic bottle Decomposes 500 years

3) if economize 1 tonne of paper you can save 17 trees """)


@bot.message_handler(commands=["whysave"])
def ws(message:Message):
    bot.send_message(message.chat.id,f"""why should save ecology?
we should save ecology because:

1) to save clean wate
                     
2) to not make new viruses
                     
3) to save clean O (oxygen)""")











bot.infinity_polling()


