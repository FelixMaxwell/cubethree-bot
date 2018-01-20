import MySQLdb

def add_hooks(client, table):
	table["quote"] = quote

conn = MySQLdb.connect(user="quotes", host="127.0.0.1", db="webserver", password=open("modules/secret.txt").read().strip())

async def quote(args, client, message):
	selector = ""
	if len(args[0]) > 1:
		selector = "%%{}%%".format(args[1])
	cur = conn.cursor()
	cur.execute("select text, author from quotes where author like %s order by rand() limit 1", (selector,))
	q = cur.fetchall()
	if len(q) == 0:
		await client.send_message(message.channel, "Could not find quote with author {}".format(args[1]))
	else:
		q = q[0]
		await client.send_message(message.channel, "{}\n\n_{}_".format(q[0], q[1]))
