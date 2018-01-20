import requests
from bs4 import BeautifulSoup
import re

regex = r"\"([^\"]+)\""

def add_hooks(client, table):
    table["wisdom"] = wisdom

def get_wisdom():
    quote = BeautifulSoup(requests.get("http://wisdomofchopra.com/iframe.php").text, "html.parser").find(id="quote").find("h2").get_text()
    return re.search(regex, quote).group(1)

async def wisdom(args, client, message):
    await client.send_message(message.channel, "_{}_".format(get_wisdom()))
