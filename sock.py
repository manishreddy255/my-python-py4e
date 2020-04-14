import socket

my_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
my_socket.connect(('data.pr4e.org', 80))
command_get = 'GET https://www.py4e.com/code3/mbox.txt HTTP/1.0\r\n\r\n'.encode()
my_socket.send(command_get)

while True:
    data = my_socket.recv(512)
    if len(data) < 1 : break
    print(data.decode())
my_socket.close()

# my_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
# my_socket.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# my_socket.send(cmd)

# while True:
#     data = my_socket.recv(512)
#     if len(data) <1: break
#     print(data.decode())
# my_socket.close()

# import urllib.request, urllib.parse , urllib.error
# data = urllib.request.urlopen('https://www.computerhope.com/jargon/w/webpage.htm')
# sort = dict()
# for lines in data:
#     decodes = lines.decode().strip()
#     print(decodes)
#     words = decodes.split()
#     for letters in words:
#         sort[letters] = sort.get(letters , 0) + 1
# item_list = sort.items()
# # print(item_list)
# ordered_list = list()
# for key,Value in item_list:
#     pairs = (Value,key)
#     ordered_list.append(pairs)
#     sorted_list = sorted(ordered_list , reverse = True)
#     # print(ordered_list)
# print(sorted_list)
# for val,key in sorted_list:
#     print(val,key)
# import urllib.request, urllib.parse , urllib.error

# open_url = urllib.request.urlopen('www.facebook.com')
# for line in open_url:
#     print(line.decode().split())

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# ctx =ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('enter:- ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# # to retrieve all anchor tagx
# tags = soup('a')
# # print(tags)
# # print(tags)
# for tag in tags:
#     print(tag.get('href', None))
# print(tags)

