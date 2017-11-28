import discord
import asyncio
from importlib import import_module
from glob import iglob

version = "1.0"

client = discord.Client()

hooks = dict()

def try_import(path):
	global hooks
	try:
		mod = import_module(path)
		funcs = set(dir(mod))
		if "add_hooks" in funcs:
			try:
				tmp_hooks = dict()
				mod.add_hooks(client, tmp_hooks)
				hooks.update(tmp_hooks)
			except Exception as e:
				print("Failed to add hooks to module {}".format(path))
				print(e, flush=True)
		print("Done loading {}".format(path), flush=True)
	except Exception as e:
		print("Failed to load module at {}".format(path))
		print(e, flush=True)

for m in iglob("./modules/**/*.py", recursive=True):
	try_import(".".join(m[2:].split(".")[0].split("/")))

async def get_info(args, client, message):
	await client.send_message(message.channel, "Cubethree Bot v{}\n{} commands registered.".format(version, len(hooks)))
hooks["info"] = get_info

from datetime import datetime
start = datetime.now()
def get_uptime():
	delta = datetime.now() - start
	return delta

async def uptime(args, client, message):
	await client.send_message(message.channel, "Uptime: {}".format(get_uptime()))
hooks["uptime"] = uptime

async def updog(args, client, message):
	await client.send_message(message.channel, "Uptime: {}".format(get_uptime()*7))
hooks["updog"] = updog

print("Registered {} commands".format(len(hooks)), flush=True)

@client.event
@asyncio.coroutine
def on_ready():
	print("Logged in as")
	print(client.user.name)
	print(client.user.id)
	print("------", flush=True)

@client.event
@asyncio.coroutine
def on_message(message):
	if not message.content.startswith("!"):
		return
	parts = message.content.split("\n")
	args = parts[0][1:].split(" ")
	args += ["\n".join(parts[1:])]
	if args[0] in hooks.keys():
		yield from (hooks[h])(args, client, message)
	else:
		yield from client.send_message(message.channel, "{} is not a command".format(args[0]))

with open("secret.txt") as fp:
	client.run(fp.read().strip())
