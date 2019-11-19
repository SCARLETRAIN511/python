from stack import stack#import the whole object
from fun1 import Classfier#import the function in that file
from linked_list import Node, SLinkedList

"""
a=stack()
a.push(2)
a.push(3)
print(a.size())
print(Classfier(a.items))
"""

def main():
    li = SLinkedList()
    li.headval = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")
    li.headval.nextval = e2
    e2.nextval = e3
    print(e2.nextval)
    print(e2.nextval.dataval)
    print(li.show())



if __name__ == "__main__":
    main()