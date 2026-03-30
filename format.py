import re

name = input("What's your name?").strip()
if matches := re.search(r"^(.+), ?(.+)$", name):
    # last, first = matches.groups()
    name = f"{matches.group(2)} {matches.group(1)}"
print(f"hello, {name}")