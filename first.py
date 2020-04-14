# print('hello world')
# n = 4
# while n > 0:
#     print(n)
#     n = n-1
# print('blast off')

# print(n)
# n = 5**4
# print(n)

# elevator = input('Europe elevator no ?: ')
# american = int(elevator) + 1
# print('US Floor is', american)

# n = 6 
# if n > 4:
#     print('yeah boty')

# for i in range(5):
#     print(i)
#     if i>2:
#         print('bigger than 2')
#     print('done with i', i)
# print('all done')

# temp = input('what do you wanna give : ')
# try:
#     tempo = int(temp)
# except:
#     tempo = 'give a valid input'

# print('first ', tempo)

# hrs = input("Enter Hours:")
# h = float(hrs)
# rate_per = input("enter rate per Hour")
# ra = float(rate_per)
# result = None
# over_work = None
# if h > 40:
#     result = h*ra
#     print(result)
#     over_work = h - 40
#     print(over_work)
#     extrapay = result+ ((over_work*ra)*1.5)
#     print(extrapay)
# else:
#     result = h*ra
#     print(result)
# score = input("Enter Score: ")
# score = float(score)
# if score >= 0.9:
#     print("A")
# elif score >= 0.8:
#     print('B')
# elif score >= 0.7:
#     print('C')
# elif score >= 0.6:
#     print('D')
# elif score < 0.6:
#     print("F")
# else:
#     print('you typed a wrong message')
#     quit()

# def king():
#     print('manny')
#     print('squibble')

# king()
# print('stubborn')
# king()

# def greeting(lang):
#     if lang == 'er':
#         print('hola')
#     elif lang == 'fr':
#         print('salut')
#     else:
#         print('you have entered the wrong keyword')
#         quit()
# greeting('er')
# hrs = input("Enter Hours:")
# rph = input("Rate per hour:")
# hrs = float(hrs)
# rph = floa(rph)
# def computepay(hour,rate):
#     if hour > 40:
#         pay = hrs - 40
#         actual_pay = (40*rph)+(pay*(rph/2))
#         return actual_pay
#     else:
#         pay = hrs*rph
#         return pay

# p = computepay(hrs,rph)
# print("Pay",p)

# finding the largest number 
# number = None
# for the_num in [5,2,3,6,12,54,32,24,76,43,21]:
#     if number is None:
#         number = the_num
#     elif the_num < number:
#         number = the_num
#         print(number)
# print('smallest number of the lot is ', number)

# #to find if the number is in the list or not and the place of it

# place = 0
# value = False
# for numbers in [1,2,34,5,3,32,55,11,65]:
#     place = place +1
#     if numbers == 3:
#         value = True
#         break
# print('the value is found at',place)
# print(value)

# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == 'done':
#         break
#     try:
#         fnum = float(num)
#     except:
#         print('invalid input')
#         continue
#     if largest is None:
#         largest = fnum
#     elif fnum > largest:
#         largest = fnum
    
#     if smallest is None:
#         smallest = fnum
#     elif fnum < smallest:
#         smallest = fnum

# print("Maximum is", largest)
# print("Minimum is", smallest)

# bob = 'banana'
# index = 0
# count = 0
# while index<len(bob):
#     print(index,bob[index])
#     if bob[index] == 'a':
#         count = count +1
#     index = index+1
# print('completed')
# print(count)
# #character slicing
# bango = 'love python'
# print(bango[0:6])
# print(bango[5:7])
# bango = 'i wanna fuck someone so special to you loveand iwanna fuck you fmor too mu little fuck'
# print(bango.count('fuck'))

# #strips the spaces and gives it a clean finish
# bango = '    sulliiga    '
# print(bango.rstrip())
# print(bango.lstrip())
# print(bango.strip())

# str1 = "hello"
# str2 = 'there'
# bob = str1+str2
# print(bob)

# x = 'from'
# print(x[0])

# text = "X-DSPAM-Confidence:    0.8475";

# print(text.find('0'))
# print(text[28])

# print(text[23:29])

# string = open('text.txt','r')
# lines = 0
# for sticker in string:
#     sticker = sticker.rstrip()
#     print(sticker)
#     lines = lines +1
# print(lines)

# inp = string.read()
# print(inp)
# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# lines = 0
# line_count = 0
# adding_number = None
# found_number = None
# for line in fh:
#     lines = lines+1
#     stagger = line.upper()
#     stagger = stagger.rstrip()
#     print(stagger)
#     if line.startswith("X-DSPAM-Confidence:") :
#         line_count = line_count+1 
#         number = line.find('0')
#         found_number = line[number:]
#         found_number = float(found_number)
#         if adding_number is None:
#             adding_number = found_number
#         elif adding_number != None:
#             adding_number = found_number + adding_number
# average = adding_number/line_count
# print(average)
# print(lines)
# print(adding_number)
# print("Done")
# print(line_count)

# x = list(range(5))
# print(x)

# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#     values = line.split()
#     for things in values:
#         if things in lst:
#             continue
#         else:
#             lst.append(things)
#     lst.sort()
# print(lst)

# fname = input("Enter file name: ")
# if len(fname) < 1 :
#     fname = "mbox-short.txt"

# fh = open(fname)
# count = 0
# for address in fh:
#     lines = address.rstrip()
#     if lines == '':
#         continue
#     words = lines.split()
#     if words[0] == 'From':
#         print(words[1])
#         count = count+1
# print("There were", count, "lines in the file with From as the first word")

# purse = dict()

# purse['lipstick'] = 1
# purse['money'] = 'No Money'
# purse['condom'] = 'yes'
# print(purse)

# sing = open('mbox-short.txt')
# count = 0
# for lines in sing:
#     count = count + lines.count('You')
# print(count)

# counts = dict()
# names = ['cwen','thug','man','thug','name','man']
# for name in names:
#     # if name not in counts:
#     #     counts[name] = 1
#     # else:
#     #     counts[name] = counts[name] + 1
#     counts[name] = counts.get(name,0) +1
# print(counts)

# print('cwen' in counts)
# file_name = input('enter the file name: ')
# repeated = dict()
# line = 0
# try:
#     file_open = open(file_name)
# except:
#     print('it is not a valid directory')
# for file_items in file_open:
#     line = line +1
#     file_lines = file_items.rstrip()
#     if file_lines == '':
#         continue
#     words = file_lines.split()
#     if words[0] == 'From':
#         mail_items = words[1]
#         # print(mail_items)
#         repeated[mail_items] = repeated.get(mail_items,0)+ 1
# print(repeated)     
# print(repeated.items())
# items = repeated.items()
# Big_number = None
# Big_word = None
# for word,number in items:
#     if Big_number is None or number > Big_number:
#         Big_word = word
#         Big_number = number

# print(Big_word,Big_number)
# # print(words)
     
    # splitted = file_items.split()
    # for splitted_items in splitted:
    #     repeated[splitted_items] = repeated.get(splitted_items,0) + 1
# print(repeated)
# values = repeated.values()
# x = max(values)
# print(x)
# print(repeated.items())
# big_count = None
# big_word = None
# for word,count in repeated.items():
#     if big_count is None or count >= big_count:
#         big_word = word
#         big_count = count
# print(big_word,big_count)
# print(line)

# tuple = (1,2,4)
# new_tuple = tuple,4,5
# print(new_tuple)

# c = {
#     'manish':6,'sundar':1,'rajan':4
# }

# temp = list()

# for x,y in c.items():
#     temp.append((y,x))
# print(temp)
# temp = sorted(temp, reverse = True)
# print(temp)

# file_input = input('which file you wannna enter : ')
# file_open = open(file_input)
# histogram = dict()
# for file_lines in file_open:
#     lines_split = file_lines.split()
#     for line_wise in lines_split:
#         histogram[line_wise] = histogram.get(line_wise,0) +1
# # print(histogram)

# histogram_list = histogram.items()
# tuple_list = list()
# for key,value in histogram_list:
#     tuples = (value,key)
#     tuple_list.append(tuples)
# sorted_list=sorted(tuple_list, reverse = True)
# # print('**** tuple list***')
# # print(sorted_list)
# for val,key in sorted_list[:10]:
#     print(key,val)
# c = {'a':10,'b':43,'c':25}
# print(sorted([(v,k) for k,v in c.items()]))

# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
# count= 0
# items = dict()
# for lines in handle:
#     lines = lines.rstrip()
#     if lines == '':
#         continue
#     splitted_lines = lines.split()
#     if splitted_lines[0] == 'From':
#         mail_data = splitted_lines[5]
#         splitted_mail_data = mail_data.split(':')
#         items[splitted_mail_data[0]] = items.get(splitted_mail_data[0],0)+1

# listing = list()
# for key,values in items.items():
#     pairs = (key,values)
#     listing.append(pairs)
# listing = sorted(listing)
# for key,value in listing:
#     print(key,value)
# print(listing)

# using regular expression
# import re
# numList = list()
# hand = open('original-data.txt')
# for line in hand:
#     line = line.rstrip()
#     stuff = re.findall('[0-9]+',line)
#     if len(stuff) == 0: continue
#     for numbers in stuff:
#         numbers_seperated = int(numbers)
#         numList.append(numbers_seperated)
# print('sum of numbers in the list is', sum(numList))


    
# x = 'My 2 favourite numbers are 10 and 35'
# y = re.findall('[0-9]+',x)
# print(y)

# the ? prefers the non- greedy so it won't try and  get the whole string in this 

# socket in python  
# mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(mySocket)
# mySocket.connect( ('data.manish.org', 80) )


# so we are gonna know how to get the data using a HTTP  request 

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #here we are having a connection
# # so we use the variable in which we stored the socket so that we can use the connect key word to connect with the server
# mysock.connect(('data.pr4e.org', 80))  #now we are connected to the server
# # now here we store what we need to send in order get the things we want 
# # so we place a get request along the encoded data
# sending_thing = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# # and at last the variable in which we stored the request is sent using the socket
# mysock.send(sending_thing)
# # Now here comes the part in which the actual data reading happens 
# while True:
#     # so when the data comes and becomes true we receive this into a variable
#     #and we receive it into a variable using recv
#     data = mysock.recv(512)
#     if (len(data)<1): break
#     # the data is decoded and then printed 
#     print(data.decode())
# #now the socket gets colosed and in the socket connection like telephone call ends 
# mysock.close()

# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')

# mysock.close()

# print(ord('a'))
# print(ord('A'))

# x = b'abc'
# print(type(x))

# my_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
# my_socket.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# my_socket.send(cmd)

# while True:
#     data = my_socket.recv(512)
#     if len(data) <1: break
#     print(data.decode())
# my_socket.close()

import mysql.connector as mysc

dbc = mysc.connect(host="localhost", user= "root", passwd= "manish143*D")
print(dbc)