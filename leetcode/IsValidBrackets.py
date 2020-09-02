#python3

class Solution:
    def isValid(self,s:str) -> bool:
        #s has the "{[()]}"
        bracketList = []
        index = 0
        isBalanced = True

        while index < len(s) and isBalanced:
            bracket = s[index]
            if bracket in "([{":
                bracketList.append(bracket)
            else:
                if bracketList == []:
                    isBalanced = False
                else:
                    match = bracketList.pop()
                    if not self.isMatch(match,bracket):
                        isBalanced = False
            index += 1
 
        
        if isBalanced and bracketList == []:
            return True
        else:
            return False

    
    def isMatch(self,b1,b2):
        if b1 == "(" and b2 == ")":
            return True
        elif b1 == "[" and b2 == "]":
            return True
        elif b1 == "{" and b2 == "}":
            return True
        else:
            return False

    def isValidBracket2(self,s) -> bool:
        stack = []
        mapping = {")":"(","}":"{","]":"["}
        for char in s:
            if char in mapping:
                topElement = stack.pop() if stack else "#"
                if mapping[char] != topElement:
                    return False
            else:
                stack.append(char)
        if stack == []:
            return True
        else:
            return False
    

if __name__ == "__main__":
    s = Solution()
    print(s.isValidBracket2("[[{{}}"))