import urllib
import urllib.request as urlreq
import json
import asyncio
import datetime

def add_hooks(client, table):
	table["!daily"] = daily 

	loop = asyncio.get_event_loop()
	future = loop.create_task(schedule_dailies(client))

async def daily(client, message):
	await daily_message(client, message.channel)

async def daily_message(client, channel):
	tmp = await client.send_message(channel, "Fetching dailies...")
	s = "\n".join(["***New set of dailies for you, hot off the presses***"] + list(get_dailies()))
	await client.edit_message(tmp, s)

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

async def schedule_dailies(client):
	while True:
		await asyncio.sleep(get_next_reset())
		await daily_message(client, client.get_channel("379181829560991744"))

loop = asyncio.get_event_loop()
