#Q: remove all the lines which contains the character 'a' in file 
# and write it to a new file

# opening a file 
file = open('file03.txt','r')
Lines = file.readlines()
#creating a new list
newLines = []

for line in Lines:
    if 'a' not in line:
        newLines.append(line)
print(newLines)

file.close()

# writing a file
with open('file04.txt','w') as file:
    for line in newLines:
        file.writelines(line)

file.close()