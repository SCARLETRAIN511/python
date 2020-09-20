positive_words=['shit','fuck','motherfucker','bullshit','idiot']
def get_pos(x):
    num_pos=0
    x_list=x.split()
    for i in x_list:
        if i in positive_words:
            num_pos+=1
    return num_pos
        
print(get_pos('I dk wtf that guy shit       idiot  shit '))