#implemention of recursion algorithms

#check the upper case in the string
def findUpperRecursive(inputStr,idx = 0):
    if inputStr[idx].isupper():
        return inputStr[idx]
    if idx == len(inputStr) - 1:
        return "No uppercase found in the give string"
    return findUpperRecursive(inputStr,idx + 1)


#calculate the length of the string:
def calStringLengthRecursive(inputStr):
    if inputStr == "":
        return 0
    return 1 + calStringLengthRecursive(inputStr[1:])


vowels = "aeiou"
note = []
def countConsonantsRecursive(inputStr):
    if inputStr == "":
        return 0
    #use the note to check whether the consonants are repeated
    if inputStr[0].lower() not in vowels and inputStr[0].isalpha() and inputStr[0].lower not in note:
        note.append(inputStr[0].lower)
        return 1 + countConsonantsRecursive(inputStr[1:])
    else:
        return countConsonantsRecursive(inputStr[1:])


#use recursion to implement the product of 2 positive integers
def mulitplyRecursive(x,y):
    if x < y:
        return mulitplyRecursive(y,x)
    if y == 0:
        return 0
    return x + mulitplyRecursive(x,y-1)



if __name__ == "__main__":
    #print(findUpperRecursive("Hello"))
    #print(calStringLengthRecursive("HelloWorld"))
    print(countConsonantsRecursive("Hello"))
    print(mulitplyRecursive(1,2))