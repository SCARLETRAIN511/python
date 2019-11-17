def solution(s1,s2):
    c1=[0]*26
    c2=[0]*26
    for i in range(len(s1)):
        pos1=ord(s1[i])-ord('a')
        c1[pos1]+=1
    for i in range(len(s2)):
        pos1=ord(s2[i])-ord('a')
        c2[pos1]+=1
    
    if c1!=c2:
        return -1
    else:
        return 1

if __name__ == "__main__":
    print(solution('cbaf','abc'))