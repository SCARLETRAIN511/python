text = ("X-DSPAM-Confidence:    0.8475");
index=text.find('0')
N=text[index:index+6]
print(float(N))