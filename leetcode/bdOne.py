t = int(input())#t lines
nums = []
for i in range(t):
    num = int(input())
    nums.append(num)
    #nums has the number -> list
sumOneCount = 0
#Sum the binary
countList = []

for num in nums:
    for dec in range(1,num + 1):
        binNum = bin(dec)[2:]
        binNum = str(binNum)
        numCount = 0
        for i in binNum:
            numCount += int(i)
        sumOneCount += numCount
    countList.append(sumOneCount)
print(sumOneCount)