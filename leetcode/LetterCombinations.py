#python3

#combinations of the letters

class Solution:
    def letterCombinations(self,digits):
        #the input is the string of the number
        keyNumber = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']}
        if digits == '':
            return []
        ans = ['']
        for num in digits:
            ans = [pre + suf for pre in ans for suf in keyNumber[num]]
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations('23'))