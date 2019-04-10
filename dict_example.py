counts=dict()
names=['sb','naocan','zz','noob','zz','nmsl']
for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)