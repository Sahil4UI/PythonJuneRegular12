#linear Search
list1=[99,10,90,11,0,55,45,-1,0]
value=int(input("enter number : "))
found=False
for item in list1:
    if(value == item):
        found=True
        break
    else:
        found=False
        
if(found==True):
    print("number found")
else:
    print("number not found")
