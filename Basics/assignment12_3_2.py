#this script is used as the practise of the scapying the informstion online using urllib
#this is the assignment for python accessing web data 12.3 assignment 2
#written by Jiaxuan Tang 12/06/2019

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
#import modules
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count=int(input('Enter the count:'))
position=int(input('Enter the position:'))
#prompt for the user's input

html = urllib.request.urlopen(url, context=ctx).read()
# Retrieve all of the anchor tags
n=0
while n<count:
    soup = BeautifulSoup(html, 'html.parser')
    tags=soup('a')
    name=tags[position-1]
    new_name=name.get('href', None)
    #This new_name will be used as new url in each iteration.
    #print out the name each time
    print(new_name)
    n+=1
    html=urllib.request.urlopen(new_name, context=ctx)
