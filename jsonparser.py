from __future__ import unicode_literals
import json
from pprint import pprint


filename = "titles.txt"
with open('hn.json') as data_file:
	parsed_json = json.load(data_file)

strings = []


for i in parsed_json:
	print(i['title'][0])

with open(filename,'wb') as f:
	for i in parsed_json:
		f.write(i['title'][0].encode('utf-8'))
		f.write('\n\n')
	




	



