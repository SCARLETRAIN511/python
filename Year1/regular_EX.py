import re
data='From Stephem.adasjdkad@uct.ac.za sat JAN'
y=re.findall('^From.*@([^ ]*)',data)
print(y)
