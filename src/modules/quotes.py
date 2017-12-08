import MySQLdb

def add_hooks(client, table):
	table["quote"] = quote

conn = MySQLdb.connect(user="quotes", host="127.0.0.1", db="webserver", password=open("modules/secret.txt").read().strip())

async def quote(args, client, message):
	cur = conn.cursor()
	cur.execute("select text, author from quotes order by rand() limit 1")
	q = cur.fetchall()[0]
	await client.send_message(message.channel, "{}\n\n_{}_".format(q[0], q[1]))
