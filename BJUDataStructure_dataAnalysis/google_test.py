
def printraw():
    raw = r'this\t\n and that'
    # this\t\n and that
    print(raw)

def printMulti():
    multi = """It was the best of times.
It was the worst of times."""
    print(multi)

def printDict():
    hash = {}
    hash['word'] = 'garfield'
    hash['count'] = 42
    s = 'I want %(count)d copies of %(word)s' % hash  # %d for int, %s for string
    print(s)
  # 'I want 42 copies of garfield'

def main():
    printMulti()
    printraw()
    printDict()
    a=5
    b=10
    answer=a+b
    print("%d + %d = %d" %(a,b,answer))

if __name__ == "__main__":
    main()
    