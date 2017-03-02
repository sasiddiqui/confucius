#Tyler

from __future__ import print_function

# process data
import json
from pprint import pprint

writeFile = open('NLCtrain.csv', 'w')

#list of json files to format, with the filename = NLC classname
list_of_files = ['python.json', 'scifi.json']

for f in list_of_files:
    with open(f) as file:
        json_data = file.read()
        items = json.loads(json_data)

        #trim the .json off
        trimmed = f.split('.')[0]

        for item in items:
            print('\'' + item['title'] + '\'' + ',' + trimmed, file = writeFile)

