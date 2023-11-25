from django.core.management.base import BaseCommand
import telebot
from champs.models import Champ

bot = telebot.TeleBot("6780147259:AAHwHK9FcAWVYePqgdPaP-xaaJTEQM1xjHE") # Вставьте сюда свой токен
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")

@bot.message_handler(commands=['champs'])
def start(message):
    champs = Champ.objects.all()
    for champ in champs:
        bot.send_message(message.chat.id, champ.name+"  "+champ.type+"   "+champ.description)
    


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f"help: /start, /champs, /add")

@bot.message_handler(commands=['add'])
def add(message):
    bot.send_message(message.from_user.id, "Введи имя чемпиона")
    bot.register_next_step_handler(message, name_handler)

def name_handler(message):
    global name
    name = message.text

    bot.send_message(message.chat.id, "Введи тип чемпиона")
    bot.register_next_step_handler(message, type_handler)


def type_handler(message):
    global type
    type = message.text

    bot.send_message(message.chat.id, "Введи описание чемпиона")
    bot.register_next_step_handler(message, desc_handler)

    

def desc_handler(message):
    global desc
    desc = message.text
    bot.send_message(message.chat.id, f"Добавился новый чемпион!")
    new_champ = Champ.objects.create(name=name, type=type, description=desc)



class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")
        
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)