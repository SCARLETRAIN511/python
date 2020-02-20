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

if __name__ == "__main__":
    #use this list as an example
    print(solution([1,2,3,5,1,3,8]))

```