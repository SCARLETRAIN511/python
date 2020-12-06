#python3

class Solution:
    def isAnagram(self,s:str,t:str)-> bool:
        if len(s) != len(t):
            return False
        strSet1 = []
        for i in s:
            strSet1.append(i)
        
        for j in t:
            if j in strSet1:
                strSet1.remove(j)
        if strSet1 != []:
            return False
        return True
