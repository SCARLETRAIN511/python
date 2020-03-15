#python3
from Array import Array

#hashtable
class Slot(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value

class HashTable(object):
    UNused = None
    Empty = Slot(None,None)

    def __init__(self):
        self._table = Array(8,init=HashTable.UNused)
        self.length = 0

    @property
    def _load_factor(self):
        return self.length/float(len(self._table))
    
    def __len__(self):
        return self.length
    
    def _hash(self,key):
        return abs(hash(key))%(len(self._table))

    def _find_key(self,key):
        index = self._hash(key)
        _len = len(self._table)
        while self._table[index] is not HashTable.UNused:
            if self._table[index] is HashTable.Empty:
                index = (index*5+1)%_len
                continue
            elif self._table[index].key == key:
                return index
            else:
                index = (index*5+1)%_len
        return None
    
    def _slot_can_insert(self,index):
        return (self._table[index] is HashTable.Empty or self._table[index] is HashTable.UNused)

    def _find_slot_for_insert(self,key):
        index = self._hash(key)
        _len = len(self._table)
        while not self._slot_can_insert(index):
            index= (index*5+1)%_len
        return index
    
    def __contains__(self, key):
        index = self._find_key(key)
        return index is not None
    
    def add(self,key,value):
        if key in self:
            index = self._find_key(key)
            self._table[index].value = value
            return False
        else:
            index = self._find_slot_for_insert(key)
            self._table[index] = Slot(key,value)
            self.length+=1
            if self._load_factor >= 0.8:
                self._rehash()
            return True
        
    def _rehash(self,key):
        old_table = self._table
        newSize = len(self._table)*2
        self._table = Array(newSize,HashTable.UNused)
        self.length = 0
        for slot in old_table:
            if slot is not HashTable.UNused and slot is not HashTable.Empty:
                index = self._find_slot_for_insert(slot,key)
                self._table[index] = slot
                self.length += 1
    def get(self,key,default = None):
        index = self._find_key(key)
        if index is None:
            return default
        else:
            return self._table[index].value
    
    def remove(self,key):
        index = self._find_key(key)
        if index == None:
            raise KeyError()
        value = self._table[index].value
        self.length -= 1
        self._table[index] = HashTable.empty
        return value
    
    def _iter_(self):
        for slot in self._table:
            if slot not in (HashTable.Empty, HashTable.UNused):
                yield slot.key
    

