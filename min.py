num_small=None#this is a flage value
L=[9,41,12,3,74,15]
for i in L:
    if num_small is None:
        num_small=i
    elif i<num_small:
        num_small=i
print(num_small)1