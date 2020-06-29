file = open('mystory.txt','r')
data = file.readlines()
newdata=[]
for line in data:
    if line.startswith('S'):
        newdata.append(line)
print(newdata)


