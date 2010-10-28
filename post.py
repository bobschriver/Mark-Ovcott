import cPickle as pickle
import oauthtwitter
import random
import sys

if len(sys.argv) == 3:
	order = sys.argv[1]
	num_values = sys.argv[2]
else:
	order = random.randint(2 , 5)
	num_values = str(random.randint(1 , order - 1))
	order = str(order)

data_directory = sys.path[0] + "/data/"

data_filename = data_directory + order + num_values + "_data"
start_sen_filename = data_directory + order + num_values + "start_sen"

data_map = pickle.load(open(data_filename))
start_sen_list = pickle.load(open(start_sen_filename))

access_token = "191210353-J9YTr34SIo0J8gFlmSlxJxjcFlkb0Ucw86NQSnvw"
access_token_secret = "OiG7X4yykQBWDUjsrFxwYPmCxhoZoLH9k1FTnCDndE"

consumer_token = "FAIfyVsiSfdGlbyu4eSA"
consumer_token_secret = "jHX6AZGoc5aCv6ueB0DDmvvjSY1U2njEQsD97SkVE"

api = oauthtwitter.OAuthApi(consumer_token, consumer_token_secret)

#request_token = api.getRequestToken()

#access_token = api.getAccessToken()

#api = oauthtwitter.OAuthApi(consumer_token, consumer_token_secret, access_tiken)

api = oauthtwitter.OAuthApi(consumer_token, consumer_token_secret, access_token , access_token_secret)

status = ""

key = random.choice(start_sen_list)
for value in key:
	status += value + " "

print key

while key in data_map and len(status) < 137:
	values = random.choice(data_map[key])
	new_key = list()

	for i in range(int(num_values), len(key)):
		new_key.append(key[i])
	
	for value in values:
		status += value + " "
		new_key.append(value)
	
	key = tuple(new_key)
	print key
	

status +=  order + num_values

count = 0

for pair in data_map:
	count += len(data_map[pair])

print status
print len(data_map)
print count

api.UpdateStatus(status)

