# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
num_c=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence: "): 
        continue
    f=line.rstrip()
    num_c=num_c+float(f[20:])
    count+=1
print('Average spam confidence:',num_c/count)

