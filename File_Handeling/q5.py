#write a menu driven python code using user defined methods  to create a textfile ->mystory.txt
#and write 5 lines in it

def writeStory(data1):
    with open('mystory.txt','w')  as file:
        for line in data1:
            file.writelines(line)
        
    file.close()
data = []
print("Enter Story Line by Line ")
for i in range(1,6):
    line= input(f"Enter line {i}:")
    data.append(line+'\n')

writeStory(data)
    

