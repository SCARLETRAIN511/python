fh = open('t.txt','r')
lst = list()
for line in fh:
    l=line.split()
    for w in l:
        if w in l:
            continue
        lst=lst.append(w)
print(lst.sort())
