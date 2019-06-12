import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter the url:')
print('Retrieving', url)

data=urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree=ET.fromstring(data)

lst=tree.findall('comments/comment')
count=len(lst)
print('Count:',count)
num_list=[]
for item in lst:
    print('number',item.find('count').text)
    num=int(item.find('count').text)
    num_list.append(num)

print(sum(num_list))



