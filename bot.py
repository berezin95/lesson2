from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import datetime, ephem

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    #print(update)
    mytext = """Привет {}!
Понимаю команду: {} 
Созвездие планеты: {} 
    """.format(update.message.chat.first_name, '/start', '/planet')

    logging.info('User {} pressed /start'.format(update.message.chat.username))

    update.message.reply_text(mytext)

    print("Вызван")

'''def chat(bot, update):
    text = update.message.text
    logging.info(text)
    update.message.reply_text(text)'''

def get_constellation(bot, update, args):
    #print(args[0])
    date = datetime.datetime.now().strftime('%Y/%m/%d')
    #print(date)
    #planet = ephem.args[0](date.strftime('%Y/%m/%d'))
    #print(ephem.constellation(planet))

    if args[0] == 'Mercury':
        planet = ephem.Mercury(date)
        result = ephem.constellation(planet)
        update.message.reply_text('{} is in constellation of {}'.format(args[0], result[1]))

    if args[0] == 'Venus':
        planet = ephem.Venus(date)
        result = ephem.constellation(planet)
        update.message.reply_text('{} is in constellation of {}'.format(args[0], result[1]))
    
    if args[0] == 'Earth':
        planet = ephem.Earth(date)
        result = ephem.constellation(planet)
        update.message.reply_text('{} is in constellation of {}'.format(args[0], result[1]))

    if args[0] == 'Mars':
        planet = ephem.Mars(date)
        result = ephem.constellation(planet)
        update.message.reply_text('{} is in constellation of {}'.format(args[0], result[1]))

    if args[0] == 'Jupiter':
        planet = ephem.Jupiter(date)
        result = ephem.constellation(planet)
        update.message.reply_text('{} is in constellation of {}'.format(args[0], result[1]))

    if args[0] == 'Saturn':
        planet = ephem.Saturn(date)
        result = ephem.constellation(planet)
        update.message.reply_text('{} is in constellation of {}'.format(args[0], result[1]))

    if args[0] == 'Uranus':
        planet = ephem.Uranus(date)
        result = ephem.constellation(planet)
        update.message.reply_text('{} is in constellation of {}'.format(args[0], result[1]))

    if args[0] == 'Neptune':
        planet = ephem.Neptune(date)
        result = ephem.constellation(planet)
        update.message.reply_text('{} is in constellation of {}'.format(args[0], result[1]))    


def main():
    updater = Updater(settings.TELEGRAM_API_KEY)
 
    updater.dispatcher.add_handler(CommandHandler("start", greet_user))
    updater.dispatcher.add_handler(CommandHandler("planet", get_constellation, pass_args=True))
    #updater.dispatcher.add_handler(MessageHandler(Filters.text, chat))
    
    updater.start_polling()
    updater.idle()

if __name__=="__main__":
    logging.info('Started')
    main()