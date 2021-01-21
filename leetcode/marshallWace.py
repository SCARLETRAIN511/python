def solution(s):
    # write your code in Python 3.6
    letters = dict()
    for i in s:
        if i not in letters.keys():
            letters[i] = 1
        else:
            letters[i] += 1
        
    
    deleteNum = 0;
    for j in letters.keys():
        if letters[j] %2 != 0:
            deleteNum += 1
    
    return deleteNum;
        

def solution2(A):
    maxNum = 0
    maxPosNag = 0

    for i in A:
        if i >= maxNum:
            print(maxNum)
            maxNum = i
            for j in A:
                if -maxNum == j:
                    maxPosNag = maxNum    
    return maxPosNag

def solution3(N):
    listStr = list(str(N))
    isNeg = 0
    if N < 0:
        isNeg = 1
        listStr = listStr[1:]

    insertIndex = 0
    #see if the num is negative or not
    if not isNeg:
        for i in range(len(listStr)):
            if int(listStr[i]) > 5:
                insertIndex += 1
            else:
                break
        listStr.insert(insertIndex,"5")
        strNum = ""
        for i in listStr:
            strNum += i
        num = int(strNum)

    else:
        for i in range(len(listStr)):
            if int(listStr[i])<5:
                insertIndex += 1
            else:
                break
        listStr.insert(insertIndex,"5")
        strNum = ""
        for i in listStr:
            strNum += i
        num = -int(strNum)
    
    return num  

if __name__ == "__main__":
    print(solution("aaxxxa"))
    print(solution2([3,2,-2,5,-3]))
    print(solution3(-2698))