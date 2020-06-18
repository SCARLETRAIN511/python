from stack import Stack

def convert_int_to_bin(dec_num):
    s = Stack()
    while dec_num > 0:
        remainder = dec_num % 2
        dec_num = dec_num // 2
        s.push(remainder)
    
    l = ""
    while not s.is_empty():
        l+=str(s.pop())
    
    return l

if __name__ == "__main__":
    print(convert_int_to_bin(1000))