import urllib
import urllib.request as urlreq
import json
import asyncio
import datetime

def add_hooks(client, table):
	table["!daily"] = daily 

	loop = asyncio.get_event_loop()
	future = loop.create_task(schedule_dailies(client))

@asyncio.coroutine
def daily(client, message):
	yield from client.send_message(message.channel, daily_string())

def daily_string():
	return "\n".join(["***New set of dailies for you, hot off the presses***"] + list(get_dailies()))

def get_dailies():
	request = urlreq.Request("https://api.guildwars2.com/v2/achievements/daily")
	with urlreq.urlopen(request) as response:
		string = response.read()
		events = json.loads(string.decode("utf-8"))["pve"]
		ids = [e["id"] for e in events if e["level"]["max"] == 80]
		request = urlreq.Request("https://api.guildwars2.com/v2/achievements?ids={}".format(
			",".join(map(lambda a: str(a), ids))
		))
		with urlreq.urlopen(request) as response2:
			return map(lambda e: e["name"], json.loads(response2.read().decode("utf-8")))

def get_next_reset():
	now = datetime.datetime.utcnow()
	return ((24 - now.hour)*60 + 1 - now.minute)*60 - now.second

@asyncio.coroutine
def schedule_dailies(client):
	while True:
		yield from asyncio.sleep(get_next_reset())
		yield from client.send_message(client.get_channel("379181829560991744"), daily_string())

loop = asyncio.get_event_loop()
