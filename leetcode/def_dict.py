from collections import defaultdict
from collections import Counter
from collections import deque

def defaultdict1():
    colors=(
        ('lxx','black'),
        ('tjx','white'),
        ('sb1','yello'),
        ('sb2','grey'),
    )
    fav_color=defaultdict(list)
    for name,color in colors:
        fav_color[name].append(color)
    print(fav_color)
    
def count1():
    colors=(
        ('lxx','black'),
        ('tjx','white'),
        ('sb1','yello'),
        ('sb2','grey'),
    )
    favs=Counter(name for name,color in colors)
    print(favs)

def deque1():
    d=deque()
    d.append('1')
    print(d[0])

if __name__ == "__main__":
    defaultdict1()
    count1()
    deque1()