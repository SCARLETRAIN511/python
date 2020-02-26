# This part is talking about greedy algorithms

----------
**typical Example**

Use python do make the script
```python
def solution(NumberList):
    NumberList.sort(reverse = True)
    MaxNum = ""
    for i in NumberList:
        MaxNum += str(i)
    MaxNum = int(MaxNum)
    return MaxNum

##使用递归解法

def efficient(NumberList):
    MaxNum = ""
    if len(NumberList) == 0:
        return ""
    else:
        maxNow = max(NumberList)
        MaxNum += str(maxNow)
        pos = NumberList.pos(maxNow)
        NumberList.pop(pos)
        return MaxNum + efficient(NumberList)


if __name__ == "__main__":
    #use this list as an example
    print(solution([1,2,3,5,1,3,8]))
    print(efficient([1,2,3,4,5,5,5]))

```