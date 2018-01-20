def add_hooks(client, table):
	table["whereami"] = whereami

def whereami(args, client, message):
	yield from client.send_message(message.channel, message.channel.id)
