#Default Function
'''
def addition():
    x=int(input("enter x"))
    y=int(input("enter y"))
    print(x+y)
addition()
'''
#Funtion with argument without return type
'''def addition(x,y):
    print(x+y)
a = int(input("Enter a : "))
b=  int(input("enter b : "))
addition(a,b)'''
#Function without argument with return type
'''def addition():
    x=int(input("enter x"))
    y=int(input("enter y"))
    return x+y
print(addition())'''
#function with argument with return type

def addition(x,y):
    return x+y
a = int(input("Enter a : "))
b=  int(input("enter b : "))
#print(addition(a,b))
result = addition(a,b)
print(result)
