from googletrans import Translator, LANGCODES
import random

lc = list(LANGCODES.values())

translator = Translator()

def add_hooks(client, table):
	table["!mangle"] = mangle

async def mangle(client, message):
	tmp_msg = "Translating..."
	tmp = await client.send_message(message.channel, tmp_msg)
	text = message.content.replace("!mangle ", "")
	for i in range(10):
		text = translator.translate(text, dest=random.choice(lc)).text
		tmp_msg += str(i+1) + "..."
		await client.edit_message(tmp, tmp_msg)
	text = translator.translate(text, dest="en").text
	await client.edit_message(tmp, text)
