fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    l=line.split()
    for w in l:
        if not w in lst:
            lst.append(w)
lst.sort()
print(lst)
