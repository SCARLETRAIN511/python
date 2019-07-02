fhandle=open('project_twitter_data.csv','r')
f=fhandle.readlines()
fhandle1=open('resulting_data.csv','w')
fhandle1.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
fhandle1.write('\n')
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@'] 
def strip_punctuation(x):
        for i in punctuation_chars:
            if i in x:
                x=x.replace(i,"")
        return x

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
pos_f.close()
def get_pos(x):
    num_pos=0
    x_list=x.split()
    for i in x_list:
        if i in positive_words:
            num_pos+=1
    return num_pos
        
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
pos_f.close()
def get_neg(x):
    num_neg=0
    x_list=x.split()
    for i in x_list:
        if i in negative_words:
            num_neg+=1
    return num_neg

for line in f[1:]:
    line=line.strip()
    line=line.split(',')
    content=line[0]
    number_retweets=line[1]
    number_replies=line[2]
    pure_content=strip_punctuation(content)
    print(pure_content)
    num_pos=get_pos(pure_content)
    num_neg=get_neg(pure_content)
    net_num=num_pos-num_neg
    row_string='{}, {}, {}, {}, {}'.format(number_retweets, number_replies, num_pos, num_neg, net_num)
    fhandle1.write(row_string)
    fhandle1.write('\n')
fhandle1.close()
fhandle.close()