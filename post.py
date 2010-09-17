import pickle
import oauthtwitter
import random

data_map = pickle.load(open("twitter-data"))

access_token = "191210353-J9YTr34SIo0J8gFlmSlxJxjcFlkb0Ucw86NQSnvw"
access_token_secret = "OiG7X4yykQBWDUjsrFxwYPmCxhoZoLH9k1FTnCDndE"

consumer_token = "FAIfyVsiSfdGlbyu4eSA"
consumer_token_secret = "jHX6AZGoc5aCv6ueB0DDmvvjSY1U2njEQsD97SkVE"

api = oauthtwitter.OAuthApi(consumer_token, consumer_token_secret, access_token , access_token_secret)

status = ""

key = random.choice(data_map.keys())
status = key[0] + " " + key[1]


while key in data_map:
	value = random.choice(data_map[key])
	status += " " + value
	key = (key[1], value)

api.UpdateStatus(status)

count = 0
for pair in data_map:
	count += len(data_map[pair])

print len(data_map)
print count
