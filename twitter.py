import re

url = input("URL: ").strip()

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)
# username = url.replace("https://twitter.com/","")
# username = url.removeprefix("https://twitter.com/")

if matches:= re.search(r"^https?://(?:www\.)?twitter.com/([a-z0-9_]+)",url, re.IGNORECASE):
    print(f"USERNAME: {matches.group(1)}")