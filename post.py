import cPickle as pickle
import oauthtwitter
import random
import sys

order = sys.argv[1]
values = sys.argv[2]

data_directory = sys.path[0] + "/data/"

data_filename = data_directory + order + values + "_data"
start_sen_filename = data_directory + order + values + "start_sen"

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
order = len(key)
num_values = len(data_map[key][0])

while key in data_map: #and len(status) < 140:
	values = random.choice(data_map[key])
	print values
	new_key = list()

	print num_values, len(key), "\n"
	for i in range(num_values, len(key)):
		new_key.append(key[i])
	
	for value in values:
		status += value + " "
		new_key.append(value)
	
	key = tuple(new_key)
	print key
	

count = 0


for pair in data_map:
	count += len(data_map[pair][0])
	#print pair
	#print data_map[pair][0]
	#print data_map[pair][1]

print status
print len(data_map)
print count

#api.UpdateStatus(status)

