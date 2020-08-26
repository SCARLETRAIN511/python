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
                print(combinations)
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backTrack(index + 1)
                    #进行回退操作，继续遍历第二个数字对应的字母
                    combination.pop()
                    #递归中的第二轮遍历完之后 再改变第一个字母，进行排列
        
        backTrack(0)
        return combinations


if __name__ == "__main__":
    s = Solution2()
    print(s.letterCombinations("23"))