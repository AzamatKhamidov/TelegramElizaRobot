import telebot
from telebot import types


bot = telebot.TeleBot('663680694:AAFCwdpHdTNroULu5prAK_8xg7YjhO7eNTo') #Token of your Bot. Get it @BotFather


where = {}

@bot.message_handler(commands = ['start'])
def start(message):
	menu = types.ReplyKeyboardMarkup(resize_keyboard = True)
	menu.row('CalKit')
	where[message.from_user.id] = 'echo'
	bot.send_message(message.chat.id, 'Hello *{}*!'.format(message.from_user.first_name), reply_markup = menu, parse_mode = 'markdown')


@bot.message_handler(content_types = ['text'])
def text(message):
	if where[message.from_user.id] == 'echo':
		if message.text == 'CalKit':
			where[message.from_user.id] = 'CalKit'
			echos = types.ReplyKeyboardMarkup()
			echos.row('Echo')
			bot.send_message(message.chat.id, 'Super CalKit :)', reply_markup = echos)
		else:
			bot.send_message(message.chat.id, message.text)
	elif where[message.from_user.id] == 'CalKit':
		if message.text == 'Echo':
			where[message.from_user.id] = 'echo'
			menu = types.ReplyKeyboardMarkup(resize_keyboard = True)
			menu.row('CalKit')
			bot.send_message(message.chat.id, 'Echo is enable', reply_markup =  menu)
		else:
			try:
				bot.send_message(message.chat.id, eval(message.text)) 
			except:
				bot.send_message(message.chat.id, 'Error')


bot.polling(True)