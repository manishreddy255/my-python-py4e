import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter url:')
open_url = urllib.request.urlopen(url)
soup = BeautifulSoup(open_url, 'html.parser')

anchor = soup("span")
number = 0
for numbers in anchor:
    number += int(numbers.contents[0])
print(number)
# import re
# import urllib.request, urllib.parse, urllib.error

# fh = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_385999.html")
# data = fh.read().decode()

# stuff = re.findall("[0-9]+", data)
# numbers = list()
# for number in stuff:
#     numbers.append(int(number))
# print(sum(numbers))