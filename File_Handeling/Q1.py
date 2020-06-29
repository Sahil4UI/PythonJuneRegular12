#Read a Text File Line By Line and display each word separated by #.
# file = open('file02.txt','r')
# data = file.readlines()
# print(data[0])
with open('file02.txt','r') as file:
    for line in file:
        line = line.replace(' ','#')
        print(line)
        # for word in line:
        #     if (word == " "):
        #         print("#",end='')
        #     else:print(word,end='')

# MULTI LINE COMMENT
'''OUTPUT :
Python#is#a#great#language#for#the#beginner-level#programmers.
Python#is#High#LEvel#General#Purpose#Programming#Language
'''