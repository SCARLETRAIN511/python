#use python to implement differemt string process algorithms

#for example 12333 can be read as one 1,one 2, three 3s, which will be converted to 111233

def nextNumber(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return "".join(result)


#spreadsheet encoding which will turn the character to number in the base of 26
def spreadSheetEncoding(colStr):
    num = 0 
    count = len(colStr) - 1
    for s in colStr:
        num += 26 ** count * (ord(s) - ord("A") + 1)
        count -= 1
    return num


#implemention of algorithms which will check the palindrome
def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            #if the char is not the alphanumeric, move the pointer forward or backward
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


#algorithms that will check whether 2 strings can be written with the same letters
def isAnagram(s1, s2):
    ht = dict()

    if len(s1) != len(s2):
        return False
    
    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1
    
    for i in ht:
        if ht[i] != 0:
            return False
    
    return True

#another algorithm is to use the letters
def isAnagram2(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()

    return sorted(s1) == sorted(s2)


def isPalindromePermu(s1,s2):
    inputStr = inputStr.replace(" ","")
    inputStr = inputStr.lower()

    d = dict()

    for i in inputStr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    oddCount = 0
    for k,v in d.items():
        #k is the key and v is the value
        if v%2 != 0 and oddCount == 0:
            oddCount += 1
        elif v%2 != 0 and oddCount != 0:
            return False
    return True


#check whether the string is unique or not
def isUnique(inputStr):
    return len(set(inputStr)) == len(input(str))


#convert integer to string
def intToStr(inputInt):
    if inputInt < 0:
        isNegative = True
        inputInt *= -1
    else:
        isNegative = False
    
    outputStr = []
    while inputInt > 0:
         outputStr.append(chr(ord('0') + inputInt % 10))
         inputInt // 10
    outputStr = outputStr[::-1]

    outputStr = "".join(outputStr)
    if isNegative:
        return '-' + outputStr
    else:
        return outputStr

#convert string to integer
def strToInt(inputStr):
    outputInt = 0

    if inputStr[0] == '-':
        startIdx = 1
        isNegative = True
    else:
        startIdx = 0
        isNegative = False
    
    for i in range(startIdx, len(inputStr)):
        place = 10**len(inputStr) - (i+1)
        digit = ord(inputStr[i]) - ord('0')
        outputInt += place * digit
    if isNegative:
        return -1 * outputInt
    else:
        return outputInt
        



if __name__ == "__main__":
    print(nextNumber("532333"))
    print(spreadSheetEncoding("AAAb"))
    print(isPalindrome("HelleH"))
    print(isAnagram2("Hello","olleh"))