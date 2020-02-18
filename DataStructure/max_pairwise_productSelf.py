# python3
#homework for week 1

def solution(NumberList):
    Sorted = sorted(NumberList)
    ans = Sorted[-2]*Sorted[-1]
    return ans


if __name__ == "__main__":
    num = int(input())
    numberList=[]
    listType = input()
    numberList = [int(x) for x in listType.split()]
    print(solution(numberList))