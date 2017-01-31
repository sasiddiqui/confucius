# process data

import json
from pprint import pprint

with open("scifi.json") as scifi:
    items = json.loads(scifi)
    scifi.close()

