import discord
import asyncio

client = discord.Client()

hooks = dict()

import gw2
import test
gw2.add_hooks(client, hooks)
test.add_hooks(client, hooks)

@client.event
@asyncio.coroutine
def on_ready():
	print("Logged in as")
	print(client.user.name)
	print(client.user.id)
	print("------")

@client.event
@asyncio.coroutine
def on_message(message):
	for h in hooks.keys():
		if message.content.startswith(h):
			yield from (hooks[h])(client, message)
			break

with open("secret.txt") as fp:
	client.run(fp.read().strip())
