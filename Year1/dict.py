def createDict():
    items1={num:num ** 2 for num in range(6)}
    items2=dict(one=1,two=2,three=3)
    items3=dict()
    items3["one"]=1
    print(items1,items2,items3)

"""
using normal way to get dict items
"""
def ModifyDict():
    list1=list()
    list2=list()
    a=dict(tjx=100,llj=1,lxx=100)
    for key,value in a.items():
        list1.append(key)
        list2.append(value)
    print("this is list 1: ", list1)
    print("this is list 2: ", list2)

"""
using generator to get items
"""
def ModifyDict2():
    list1=list()
    list2=list()
    a=dict(tjx=100,llj=1,lxx=100)
    list1=[item for item in a.keys()]
    list2=[item for item in a.values()]
    print("this is list 1 using generator: ",list1)
    print("this is list 2 using generator: ",list2)

def main():
    ModifyDict()
    ModifyDict2()

if __name__ == "__main__":
    main()


    