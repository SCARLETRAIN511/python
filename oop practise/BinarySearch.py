#implemention of binary search

#this is the linear search
def linearSearch(target,data):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

#implemention of binary search
def binarySearchIterative(target,data):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) //2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
            


def main():
    print(linearSearch(3,[12,3,4,22]))
    print(binarySearchIterative(3,[12,3,4,22]))


if __name__ == "__main__":
    main()