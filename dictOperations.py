import requests
import json

def write():
    data = requests.get("https://www.py4e.com/code3/mbox.txt")
    lines = data.content.decode()

    with open("original_text.txt", "w") as f:
        f.write(lines)

