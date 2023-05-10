# this glitch is patched, it will not work!

USERNAME = "d329"
PASSWORD = "lol no"

import time
import random
import scratchattach
events = scratchattach.CloudEvents(669020072)
conn = scratchattach.login(USERNAME, PASSWORD).connect_cloud(669020072)

@events.event
def on_set(event):
	if not (event.user == "yippymishy") and not (event.user == 'd329'):
		if (event.value == '232143'): # balance
			conn.set_var("Cloud", scratchattach.Encoding.encode(event.user)+"80197519") # user + "$0.0"
			time.sleep(0.15)
			randy = random.randint(9999999,99999999)
			conn.set_var("Cloud", scratchattach.Encoding.encode(f"give&{event.user}$report-this-glitch-by-commenting-{randy}-$yippymishy${randy}&0"))

		if (event.value == '2349215527'): # leaderboard
			conn.set_var("Cloud", "69375151694537573569911996693751516945375735699119966937515169453757356991199669375151694537573569911996693751516945375735699119")
			# yippymishy#0&yippymishy#0&yippymishy#0&yippymishy#0&yippymishy#0

		if ('57292996' in event.value): # admin see balance
			conn.set_var("admin", "57292923214380197519")
			# seebal$0.0

		print(event.user + ": " + scratchattach.Encoding.decode(event.value)) # prints request user made

@events.event
def on_ready():
	print("swag")

events.start()
