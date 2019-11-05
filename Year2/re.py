import re
#regular expressions

def main():
    str = 'an example word:cat!!'
    match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
    if match:
        print('found', match.group()) ## 'found word:cat'
    else:
        print('did not find')

    email="Jiaxuan.Tang18@imperial.ac.uk"
    match=re.search(r"[\w.-]+@[\w.-]+",email)
    #greedy using +
    if match:
        print(match.group())
    #using findall with re
    str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
    tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
    print(tuples)  ## [('alice', 'google.com'), ('bob', 'abc.com')]

if __name__ == "__main__":
    main()
