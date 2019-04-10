abc='what the fuck'
i=abc.split()
for word in i:
    if word.startswith('fuck') is True:
        print(word)
