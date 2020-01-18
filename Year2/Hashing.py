#new data structure called hashing
#hash table is a kind of data set
#every position in hashing table is called slot(槽)

#however collision is a problem
#对字符串进行散列函数 
def hash(astring, tableSize):
    sum = 0
    for pos in range(len(astring)):
        sum += ord(astring[pos])
    return sum