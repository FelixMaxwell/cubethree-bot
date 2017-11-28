import urllib
import urllib.request as urlreq
import asyncio

def add_hooks(client, table):
	table["!inspire"] = inspire

async def inspire(client, message):
	tmp = await client.send_message(message.channel, "Fetching image...")
	request = urlreq.Request("http://inspirobot.me/api?generate=true")
	request.add_header("Host", "inspirobot.me")
	request.add_header("User-Agent", "cubethree-bot")
	request.add_header("Contact", "felixmaxwell@comcast.net")
	request.add_header("Accept", "*/*")
	with urlreq.urlopen(request) as response:
		string = response.read().decode("utf-8")
		await client.edit_message(tmp, string)
