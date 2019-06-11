import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count=int(input('Enter the count:'))
position=int(input('Enter the position:'))
html = urllib.request.urlopen(url, context=ctx).read()
# Retrieve all of the anchor tags
n=0
while n<count:
    soup = BeautifulSoup(html, 'html.parser')
    tags=soup('a')
    name=tags[position-1]
    new_name=name.get('href', None)
    print(new_name)
    n+=1
    html=urllib.request.urlopen(new_name, context=ctx)
