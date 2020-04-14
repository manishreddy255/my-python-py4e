import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx =ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count = 0
url = input('Enter url: ')
positon = input('Enter position:')
positon = int(positon)
given_count = input('Enter count: ')
given_count = int(given_count)
while True:
    linking = urllib.request.urlopen(url)
    soup = BeautifulSoup(linking , 'html.parser')

    tags = soup('a')
    listed = list()
    for tag in tags:
        link = tag.get('href', None)
        listed.append(link)
    required_link = listed[positon-1]
    print('Retrieving:',url)
    count = count +1
    if count == given_count+1:
        splitting_1 = url.split('_')
        new_url = splitting_1[2]
        splitting_new_url = new_url.split('.')
        print(splitting_new_url[0])
        break
    
    url = required_link
