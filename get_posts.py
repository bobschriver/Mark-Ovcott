import twitter
import pickle
import os
import HTMLParser

num_results = 200

search_terms = ['tcot' , 'teaparty' , 'wreckingcrew' , 'twisters']

data_filename = "/users/u16/schriver/projects/personal/mark_ovcott/twitter-data"
last_search_filename = "/users/u16/schriver/projects/personal/mark_ovcott/last_search_time"


if not os.path.exists(data_filename):
	data_map = dict()
else:
	data_map = pickle.load(open(data_filename))

if not os.path.exists(last_search_filename):
	last_search_time_map = {}
else:
	last_search_time_map = pickle.load(open(last_search_filename))

api = twitter.Api()
html_parser = HTMLParser.HTMLParser()

for search_term in search_terms:
	if search_term in last_search_time_map:
		last_search_time = last_search_time_map[search_term]
		statuses = api.GetSearch(search_term, None, last_search_time, num_results)
	else:
		statuses = api.GetSearch(search_term , None , None ,  num_results)
	
	print len(statuses)
	
	last_search_time_map[search_term] = statuses[-1].GetId()

	for status in statuses:
		text = status.GetText()
		words = text.split()
		for i in range( len(words) - 2):
			word_one = html_parser.unescape(words[i])
			word_two = html_parser.unescape(words[i+1])
			word_three = html_parser.unescape(words[i+2])
			key = (word_one , word_two)
			value = word_three
			
			if key in data_map:
				data_map[key].append(value)
			else:
				data_map[key] = [value]

pickle.dump(data_map , open(data_filename , "w"))
pickle.dump(last_search_time_map , open(last_search_filename, "w"))



