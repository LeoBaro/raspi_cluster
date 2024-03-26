import telebot
import argparse

from utils import get_ip

def main(args):
	
	with open(args.token_file, "r") as tf:
		token = tf.read().strip()

	bot = telebot.TeleBot(token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

	@bot.message_handler(commands=['start', 'help'])
	def send_welcome(message):
		bot.reply_to(message, "Howdy, send /ip to get my IP address")

	@bot.message_handler(commands=['ip'])
	def get_ip_address(message):
		bot.reply_to(message, f"My IP address is: {get_ip()}")

	bot.infinity_polling()


def cli():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--token-file", type=str, required=True)
	return parser.parse_args()

if __name__=='__main__':
	main(cli())