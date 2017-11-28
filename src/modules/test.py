def add_hooks(client, table):
	table["!whereami"] = whereami

def whereami(client, message):
	yield from client.send_message(message.channel, message.channel.id)
