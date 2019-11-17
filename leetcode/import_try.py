from stack import stack#import the whole object
from fun1 import Classfier#import the function in that file

a=stack()
a.push(2)
a.push(3)
print(a.size())
print(Classfier(a.items))