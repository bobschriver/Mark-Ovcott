import twitter
import pickle
import os
import HTMLParser
import gc

gc.disable()

num_results = 100
script_dir = "/users/u16/schriver/projects/personal/mark_ovcott/"


search_terms = ['#tcot' , '#teaparty' , '#wreckingcrew' , '#twisters' , '#gop' , '#ocra' , '#sgp']

data_filename = "twitter-data"
last_search_filename = "last_search_time"

data_filename_abs = script_dir + data_filename
last_search_filename_abs = script_dir + last_search_filename


if not os.path.exists(data_filename_abs):
	data_map = dict()
else:
	data_map = pickle.load(open(data_filename_abs))

if not os.path.exists(last_search_filename_abs):
	last_search_time_map = {}
else:
	last_search_time_map = pickle.load(open(last_search_filename_abs))

api = twitter.Api()
html_parser = HTMLParser.HTMLParser()

previous_statuses = []

for search_term in search_terms:
	if search_term in last_search_time_map:
		last_search_time = last_search_time_map[search_term]
		statuses = api.GetSearch(search_term, None, last_search_time, num_results)
	else:
		statuses = api.GetSearch(search_term , None , None ,  num_results)
	
	#print len(statuses)
	
	last_search_time_map[search_term] = statuses[-1].GetId()
	
	for status in statuses:
		if status not in previous_statuses:
			previous_statuses.append(status)
			text = status.GetText()
			words = text.split()
			for i in range( len(words) - 2):
				word_one = html_parser.unescape(words[i])
				word_two = html_parser.unescape(words[i+1])
				word_three = html_parser.unescape(words[i+2])
						
				key = (word_one , word_two)
				value = word_three				
				
				start_sen_count = 1 if i == 0 else 0
						
				if key in data_map:
					start_sen_count += data_map[key][1]
					
					data_map[key] = [data_map[key][0].append(value) , start_sen_count]
				else:
					data_map[key] = [[value] , start_sen_count]


pickle.dump(data_map , open(data_filename_abs , "w"))
pickle.dump(last_search_time_map , open(last_search_filename_abs, "w"))
