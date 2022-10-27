import telebot
import extensions as ext
import logging

logging.basicConfig(filename='bot.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = '5785057704:AAGHT9myr2PwDuCvG-NkjEL1qT1MGc1psbw'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    message_text = """
        доступные команды:
        /value - отобразить список кодов валют
        cr1 cr2 NNNN - произвести рассчет курса NNNN валюты cr в валюту cr2
    """
    bot.reply_to(message, message_text)

@bot.message_handler(commands=['value'])
def handle_start_help(message):
    ext.renew_values()
    message_text = 'коды доступных валют: \n'
    for cur in ext.currency:
        message_text +=  ext.currency[cur].code + ' - ' + str(ext.currency[cur].nominal) + ' ' + ext.currency[cur].name + "\n"
    bot.send_message(message.chat.id, message_text)


@bot.message_handler(regexp ='[a-zA-Z]{3} [a-zA-Z]{3} [0-9]+')
def handle_start_help(message):
    args = message.text.split()
    cur1 = args[0].upper()
    cur2 = args[1].upper()
    amount = int(args[2])
    message_text = ext.calculate(cur1, cur2, amount)
    bot.send_message(message.chat.id, message_text)

#bot.polling(none_stop=True)

bot.infinity_polling()