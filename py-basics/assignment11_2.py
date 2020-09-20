import re
numlist=list()
hand=open('actual_data.txt')
for line in hand:
    line=line.strip()
    number=re.findall('([0-9]+)',line)
    if len(number) == 0:
        continue
    nlist=list(map(int,number))
    numlist.extend(nlist)
print(sum(numlist))

