from googletrans import Translator, LANGCODES
import random

translator = Translator()

def add_hooks(client, table):
	table["!mangle"] = mangle

def mangle(client, message):
	text = message.content.replace("!mangle ", "")
	for i in range(10):
		text = translator.translate(text, dest=random.choice(LANGCODES.values())).text
	text = translator.translate(string, dest="en").text
	yield from client.send_message(message.channel, text)
