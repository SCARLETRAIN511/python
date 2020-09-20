import json
import requests
page=requests.get("http://api.datamuse.com/words?rel_rhy=funny")
print(type(page))
print(page.text[:150])
print(page.url)
print('------')
x=page.json()#alternative x=json.loads(page.txt)
print(type(x))
print('first item in the list')
print(x[0])
print('The whole text')
print(json.dumps(x,indent=2))
