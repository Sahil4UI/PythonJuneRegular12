#write  a binary file ,check for a given rollNo, and print the corresponding Name

RollNo = [101,102,103,104,105]
Name = ["Ram","Amit","Krish","Shyam","Amit"]
Marks = [98,90,87,70,50]
choice = int(input("Enter the RollNo : "))
found=pos = 0
#Searching
for i in range(0,len(RollNo)):
    if(choice == RollNo[i]):
        found = 1
        pos = i
        break

newMarks = input("Enter  updated Marks: ")
Marks[pos] = newMarks
print(Name)

'''
if (found == 0):
    print("Not found")
else:
    print(Name[pos])

'''

    
        

