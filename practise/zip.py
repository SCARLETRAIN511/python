l=[1,2,3]
l2=[2,21,31]
print(list(zip(l,l2)))
l3=[x1+x2 for (x1, x2) in list(zip(l,l2))]
print(l3)