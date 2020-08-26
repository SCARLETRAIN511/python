#python3

class Solution:
    def letterCombinations(self,digits:str):
        #the input is the string of the number

        keyNumber = {"2":['a','b','c'],
                    "3":['d','e','f'],
                    "4":['g','h','i'],
                    "5":['j','k','l'],
                    "6":['m','n','o'],
                    "7":['p','q','r','s'],
                    "9":['t','u','v'],
                    "10":['w','x','y','z']}
        
        if digits == "":
            return []
        
        ans = [""]
        for num in digits:
            ans = [pre + suf for pre in ans for suf in keyNumber[num]]
        return ans


class Solution2:
    def letterCombinations(self,digits:str):
        if not digits:
            return list()
        
        combination = []
        combinations = []

        phoneMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        def backTrack(index:int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backTrack(index + 1)
                    combination.pop()
        
        backTrack(0)
        return combinations


if __name__ == "__main__":
    s = Solution2()
    print(s.letterCombinations("23"))