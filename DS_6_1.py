name = input("Enter file:")
d=dict()
if len(name) < 1 : 
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line=line.strip()
    wds=line.split()
    if len(wds)<1:
        continue
    if wds[0]!='From':
        continue
    time=wds[5]
    pieces=time.split(':')
    hour=pieces[0]
    d[hour]=d.get(hour,0)+1
for k,v in sorted(d.items()):
    print(k,v)