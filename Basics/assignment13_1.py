import json
import urllib.request, urllib.parse, urllib.error
import ssl


url=input('Enter location:')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data=urllib.request.urlopen(url,context=ctx).read()


num_list=[]
info=json.loads(data)

for item in info["comments"]:
    print('Name:', item['name'])
    print('count:', item['count'])
    num_list.append(int(item["count"]))
print(sum(num_list))