# Uses python3
import sys
import random
 
def partition3(a, l, r):
    #write your code here
    x = a[l]
    lhs = l
    rhs = r
    i = l
    while i <= rhs:
        if a[i] <= x:
            a[i],a[lhs] = a[lhs],a[i]
            lhs += 1
            i += 1
        elif a[i] > x:
            a[i],a[rhs] = a[rhs],a[i]
            rhs -= 1
        else:
            i += 1
    return lhs, rhs


def randomized_quick_sort(a, l, r):
    while l <= r:
        k = random.randint(l,r)
        a[l],a[k] = a[k],a[l]

        m1, m2 = partition3(a,l,r)
        if (m1 - l) < (m2 - l):
            randomized_quick_sort(a, l, m1-1)
            l = m2 + 1
        else:
            randomized_quick_sort(a,m2+1,r)
            r = m1 - 1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
