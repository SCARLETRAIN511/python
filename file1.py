fh = open('t.txt','r')
lst = list()
for line in fh:
    l=line.split()
    for w in l:
        if not w in lst:
            continue
        lst=lst.append(w)
lst.sort()
print(lst)
