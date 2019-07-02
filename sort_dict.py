def last_four(x):
    j=str(x)
    k=j[-4:]
    return k

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids=sorted(ids,key=last_four)
print(sorted_ids)