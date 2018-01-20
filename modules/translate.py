from googletrans import Translator, LANGCODES
import random

lc = list(LANGCODES.values())

translator = Translator()

def add_hooks(client, table):
	table["mangle"] = mangle
	table["translate"] = translate

async def mangle(args, client, message):
	try:
			times = int(args[1])
			text = " ".join(args[2:-1]) + "\n" + args[-1]
	except:
		times = 10
		text = " ".join(args[1:-1] + "\n" + args[-1])
	tmp_msg = "Translating..."
	tmp = await client.send_message(message.channel, tmp_msg)
	for i in range(times):
		text = translator.translate(text, dest=random.choice(lc)).text
		tmp_msg += str(i+1) + "..."
		await client.edit_message(tmp, tmp_msg)
	text = translator.translate(text, dest="en").text
	await client.edit_message(tmp, text)

async def translate(args, client, message):
	tmp = await client.send_message(message.channel, "Translating...")
	text = translator.translate(" ".join(args[1:-1]) + "\n" + args[-1], dest="en").text
	await client.edit_message(tmp, text)
