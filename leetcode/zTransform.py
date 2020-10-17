#python3

class Solution:
    def convert(self,s,numRows) -> str:
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i,flag = 0, - 1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        
        return "".join(res)


if __name__ == "__main__":
    s = Solution()
    print(s.convert("Hellodadj",4))