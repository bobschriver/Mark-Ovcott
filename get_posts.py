import twitter
import cPickle as pickle
import os
import HTMLParser
import re
import sys
import unicodedata
import string
import random

if len(sys.argv) == 2:
	order = int(sys.argv[1])
	values = int(sys.argv[2])
else:
	order = random.randint(2 , 5)
	values = random.randint(1 , order - 1)

num_results = 100
search_terms = ['#tcot' , '#teaparty' , '#wreckingcrew' , '#twisters' , '#gop' , '#ocra' , '#sgp']

data_dir = sys.path[0] + "/data/"
file_prefix = str(order) + str(values)

data_filename = file_prefix + "_data"
last_search_filename = file_prefix + "last_search"
start_sen_filename = file_prefix + "start_sen"

data_filename_abs = data_dir + data_filename
last_search_filename_abs = data_dir + last_search_filename
start_sen_filename_abs = data_dir + start_sen_filename


if not os.path.exists(data_filename_abs):
	data_map = dict()
else:
	data_map = pickle.load(open(data_filename_abs))

if not os.path.exists(last_search_filename_abs):
	last_search_time_map = dict()
else:
	last_search_time_map = pickle.load(open(last_search_filename_abs))

if not os.path.exists(start_sen_filename_abs):
	start_sen_list = list()
else:
	start_sen_list = pickle.load(open(start_sen_filename_abs))

api = twitter.Api()
html_parser = HTMLParser.HTMLParser()

previous_statuses = []

for search_term in search_terms:
	if search_term in last_search_time_map:
		last_search_time = last_search_time_map[search_term]
		statuses = api.GetSearch(search_term, None, last_search_time, num_results)
	else:
		statuses = api.GetSearch(search_term , None , None ,  num_results)
	
	last_search_time_map[search_term] = statuses[-1].GetId()
	
	for status in statuses:		
		if status.GetText() not in previous_statuses: 
			#Make sure we don't add duplicate posts
			previous_statuses.append(status.GetText())
			
			#lets first convert the text to something we can deal with
			text = status.GetText()
	
			#This is kinda a hack untill I can get the two lines below to
			#work properly.
			text = "".join(c for c in text if c in string.printable)
			text = html_parser.unescape(text)
			unicodedata.normalize("NFKD" , text).encode("ascii", "ignore")
			
			text = text.lower()
			
			#remove URL's
			text = re.sub("(http://)?(www\.)?\w+\.\w{2,3}.*\s", " " , text)
			#Remove useless symbols
			text = re.sub("[~`_^+]" , "" , text)
			#Remove any doubled non word characters
			text = re.sub("([^a-zA-Z0-9])\\1+" , "\\1" , text)
			#Remove opening/closing punctuation so we don't have random open parens etc
			text = re.sub("[\*\[\]\(\)\<\>]", "" , text)
			#replace current word seperators with spaces
			text = re.sub("(\w)[\|\-\=\/\\\](\w)" , "\\1 \\2", text)
			#Put a space between the end of sentences
			text = re.sub("(\w)([\.\?\!\,\:\;])(\w)", "\\1\\2 \\3", text) 
			#Split any current adjacent symbols
			text = re.sub("([^a-zA-Z0-9 ])([^a-zA-Z0-9 ])" , "\\1 \\2" , text)

			words = text.split()

			for i in range( len(words) - (order + values)):
				key = []
				value = []

				for j in range(order):
					key.append(words[i + j])
				
				for j in range(order , order + values):
					value.append(words[i+j])
	
				key = tuple(key)
				value = tuple(value)		

				if i == 0:
					start_sen_list.append(key)
						
				if key not in data_map:
					data_map[key] = []
				
				data_map[key].append(value)


print data_map


pickle.dump(data_map , open(data_filename_abs , "w"))
pickle.dump(last_search_time_map , open(last_search_filename_abs, "w"))
pickle.dump(start_sen_list, open(start_sen_filename_abs , "w"))
