name = input("Enter file:")
d=dict()
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line=line.strip()
    words=line.split()
    if len(words)<1:
        continue
    if words[0]!='From':
        continue
    d[words[1]]=d.get(words[1],0)+1
bigcount=None
bigword=None
for word,count in d.items():
    if bigcount==None or bigcount<count:
        bigword=word
        bigcount=count
print(bigword,bigcount)
