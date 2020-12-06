#python3

class Solution:
    def isAnagram(self,s:str,t:str)-> bool:
        strSet = set()
        for i in s:
            strSet.add(i)
        
        for j in t:
            if j not in strSet:
                return False

        return True
