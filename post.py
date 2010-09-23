import pickle
import oauthtwitter
import random

def select_weighted():
	total = 0
	for key in data_map:
		total += data_map[key][1] * 2
	
	for key in data_map:
		rand_num = random.uniform(0,1)
		acc_prob = 1.0 / (total - (data_map[key][1]*2)^2)
		if rand_num <= acc_prob:
			return key

	return random.choice(data_map.keys())

script_directory = "/users/u16/schriver/projects/personal/mark_ovcott/"

data_map = pickle.load(open(script_directory + "twitter-data"))

access_token = "191210353-J9YTr34SIo0J8gFlmSlxJxjcFlkb0Ucw86NQSnvw"
access_token_secret = "OiG7X4yykQBWDUjsrFxwYPmCxhoZoLH9k1FTnCDndE"

consumer_token = "FAIfyVsiSfdGlbyu4eSA"
consumer_token_secret = "jHX6AZGoc5aCv6ueB0DDmvvjSY1U2njEQsD97SkVE"

api = oauthtwitter.OAuthApi(consumer_token, consumer_token_secret)

#request_token = api.getRequestToken()

#access_token = api.getAccessToken()

#api = oauthtwitter.OAuthApi(consumer_token, consumer_token_secret, access_tiken)

api = oauthtwitter.OAuthApi(consumer_token, consumer_token_secret, access_token , access_token_secret)

#status = ""

key = select_weighted()
status = key[0] + " " + key[1]

print key
print data_map[key][1]

while key in data_map and len(status) < 140:
	value = random.choice(data_map[key][0])
	status += " " + value
	key = (key[1], value)

count = 0


for pair in data_map:
	count += len(data_map[pair])
	#print pair
	#print data_map[pair][0]
	#print data_map[pair][1]

print status
print len(data_map)
print count

#api.UpdateStatus(status)

