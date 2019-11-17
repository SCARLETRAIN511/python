class Node:

    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

    def get_data(self):
        return self.dataval

    def set_data(self,new_data):
        self.dataval=new_data

    def get_next(self):
        return self.nextval

    def set_next(self,new_next):
        self.nextval=new_next

class SLinkedList:

    def __int__(self):
        self.headval=None

    def add(self,dataval):
        new_node=Node(dataval)
        new_node.set_next(self.headval)
        self.headval=new_node

    def search(self,dataval):
        checking=self.headval
        while checking !=None:
            if checking.get_data()==dataval:
                return True
            checking=checking.get_next()
        return False

    def remove(self,dataval):
        checking=self.headval
        previous=None
        while checking !=None:
            if checking.get_data()==dataval:
                break
            previous=checking
            checking=checking.get_next()
        if previous == None:
            self.headval=checking.get_next()
        else:
            previous.set_next(checking.get_next())

    def isEmpty(self):
        return self.headval==None
    
    def size(self):
        count=0
        counting=self.headval
        while counting!=0:
            count+=1
            counting=counting.get_next()
        return count



