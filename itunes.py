import requests
import sys
import json

if len(sys.argv) < 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=100&term=" + sys.argv[1])
obj = response.json()
for i in obj["results"]:
    print(i["trackName"])