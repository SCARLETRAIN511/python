
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
def second(x):
    y=[]
    for i in x:
        y.append(i[1])
    return y
second_let=second(ex_lst)
print(second_let)
func_sort=sorted(second_let)
print(func_sort)