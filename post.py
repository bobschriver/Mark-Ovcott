import pickle

data_map = pickle.load(open("twitter-data"))


count = 0
for pair in data_map:
	print pair
	print data_map[pair]
	count += len(data_map[pair])

print len(data_map)
print count
