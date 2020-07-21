#python3

#count and say 描述数

class Solution:
    #double poinmters method
    def countAndSay(self,n) -> str:
        prevPerson = "1"
        for i in range(1,n):
            nextPerson,num,count = "",prevPerson[0],1
            for j in range(1,len(prevPerson)):
                #如果出现的数一致，数量 + 1
                if prevPerson[j] == num:
                    count += 1
                #如果不一致，先添加已有的描述，更换数字与次数
                else:
                    nextPerson += (str(count) + num)
                    num = prevPerson[j]
                    count = 1
            nextPerson += str(count) + num
            prevPerson = nextPerson
        return prevPerson


if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(4))