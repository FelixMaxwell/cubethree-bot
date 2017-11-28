import discord
import asyncio

version = "1.0"

client = discord.Client()

hooks = dict()

import gw2
import test
import rando
import translate
import inspire
gw2.add_hooks(client, hooks)
test.add_hooks(client, hooks)
rando.add_hooks(client, hooks)
translate.add_hooks(client, hooks)
inspire.add_hooks(client, hooks)

async def get_info(client, message):
	await client.send_message(message.channel, "Cubethree Bot v{}\n{} commands registered.".format(version, len(hooks)))
hooks["!info"] = get_info

from datetime import datetime
start = datetime.now()
def get_uptime():
	delta = datetime.now() - start
	return delta

async def uptime(client, message):
	await client.send_message(message.channel, "Uptime: {}".format(get_uptime()))
hooks["!uptime"] = uptime

async def updog(client, message):
	await client.send_message(message.channel, "Uptime: {}".format(get_uptime()*7))
hooks["!updog"] = updog

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
