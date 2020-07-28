#python3

class Solution:
    digits = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,"IV"),(1,'I')]
    def intToRoman(self,num) -> str:
        romanDigits = []
        for value,symbol in self.digits:
            if num == 0:
                break
            count,num = divmod(num,value)
            romanDigits.append(symbol*count)
        return "".join(romanDigits)     

if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(58))   
