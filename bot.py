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
Посчитать количество слов: {}
    """.format(update.message.chat.first_name, '/start', '/planet', '/wordcount')

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

def words_number(bot, update, args):
    print(args)
    #print(update)
    
    if args == []:
        update.message.reply_text('Ничего не ввел')
    else:
        last_word = args[len(args)-1]
        first_symbol = args[0][0]
        last_symbol = last_word[len(last_word)-1]
        if first_symbol != '"' or last_symbol != '"':
            update.message.reply_text('Введи текст в двойных кавычках')
        else:
            num_of_words = len(args) - args.count('-')
            update.message.reply_text('Кол-во слов - {}'.format(num_of_words))

    
def calculate(bot, update):
    operations = ['+','-','*','/']
    user_input = update.message.text
    

    if user_input[len(user_input)-1] == "=":
        user_input = user_input[:-1]
        if (user_input[:1] in operations) or (user_input[-1:] in operations) or (' ' in user_input) or (user_input == ''):
            update.message.reply_text("Введите числа или уберите пробелы")
        else:
            try:
                if(user_input.find('+') != -1):
                    first_number = int(user_input.split('+')[0])
                    second_number = int(user_input.split('+')[1])
                    update.message.reply_text(first_number + second_number)
                elif (user_input.find('-') != -1):
                    first_number = int(user_input.split('-')[0])
                    second_number = int(user_input.split('-')[1])
                    update.message.reply_text(first_number - second_number)
                elif (user_input.find('*') != -1):
                    first_number = int(user_input.split('*')[0])
                    second_number = int(user_input.split('*')[1])
                    update.message.reply_text(first_number * second_number)
                elif (user_input.find('/') != -1):
                    first_number = int(user_input.split('/')[0])
                    second_number = int(user_input.split('/')[1])
                    update.message.reply_text(first_number / second_number)
            except(ZeroDivisionError):
                update.message.reply_text('Деление на 0')

        sign_id = user_input.find()
    else:
        update.message.reply_text(user_input)

def main():
    updater = Updater(settings.TELEGRAM_API_KEY)
 
    updater.dispatcher.add_handler(CommandHandler("start", greet_user))
    updater.dispatcher.add_handler(CommandHandler("planet", get_constellation, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler("wordcount", words_number, pass_args=True))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, calculate))
    #updater.dispatcher.add_handler(MessageHandler(Filters.text, chat))
    
    updater.start_polling()
    updater.idle()

if __name__=="__main__":
    logging.info('Started')
    main()