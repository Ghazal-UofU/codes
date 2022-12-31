#30.12.2022
#Ghazal_UofU
#Python standard libraries


#Modules (libraries) are comprised of a set of functions that can be imported.
#PSL (Python Standard Libraries) is a set of libraries

#random

import random


#while True:
w= random. randint (0, 100)     # a rand in d range of 0 to 100
print(w)


import datetime

#from datetime import date (from module  import submodule)
_ = datetime.date.today()
print(_)

print(_)


#if u want to import 2 methods of a library just write like this:
    #A.C()
    #B.C()

#othrwise import the whole librar like this:
    #import C


print('-----------------------------------------------------------')

import os

_ = os.getcwd()    #get current  working directory
print(_)

#make directory
#os.mkdir()



#os.walk()      #reading the whole directory like a tree


#os.listdir     #returns all of the files in the directory

print(os.listdir())

print('-----------------------------------------------------------')

import time

print (time.time())     #number of seconds from the reference point (epok), which the ref time is time.gmtime (0)

print(time.gmtime(0))

print('-----------------------------------------------------------')


print(time.ctime())     #current date and time

print(time.ctime(time.time()))  #date and time

print(time.sleep(5))    #the program waits for 5 sec (a delay)


for i in range (10, 100, 10):
    print(i)
    time.sleep(2)



