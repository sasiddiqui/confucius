# process data

import json
from bs4 import BeautifulSoup
from pprint import pprint

with open("scifi.json") as scifi:
    json_data = file.read(scifi)
    items = json.loads(json_data)
    scifi.close()
