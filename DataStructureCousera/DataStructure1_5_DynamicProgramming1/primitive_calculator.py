# Uses python3
import sys

def optimal_sequence(n):
    min_num_operations = [n] * n
    min_num_operations[0] = 0

    ops = [-1]*n
    op_types = (1,2,3)
    for i in range(n-1):
        for op_type in op_types:
            n_i = i + 1
            if op_type == 1:
                n_new = n_i * 2
            elif op_type == 2:
                n_new = n_i *3
            elif op_type == 3:
                n_new = n_i + 1
            else:
                raise ValueError('New operation type {}'.format(op_type))
            num_operations = min_num_operations[i] + 1
            i_new = n_new - 1
            
            if n_new <= n and num_operations<min_num_operations[i_new]:
                min_num_operations[i_new] = num_operations
                ops[i_new] = op_type
    seq = getSequence(n,ops)
    return seq

def getSequence(n,ops):
    n_seq = n
    seq = [n]
    while n_seq != 1:
        i = n_seq - 1
        op_type = ops[i]
        if op_type == 1:
            n_seq = n_seq//2
        elif op_type == 2:
            n_seq = n_seq//3
        elif op_type == 3:
            n_seq = n_seq - 1
        else:
            raise ValueError("New operation type{}".format(op_type))
        seq.append(n_seq)
    return seq[::-1]


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
