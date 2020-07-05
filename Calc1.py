#default function (fn without argument without return type)
#fn without argument with return type
#fn with argument without return type
#fn with argument with return type
#menu based Calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
    
x = int(input("Enter the first Number: "))
y = int(input("Enter the second Number: "))
print('''
Press + for addition
Press - for subtraction
Press * for Multiplication
Press / for Division
''')
choice = input("Enter Choice: ")
dictionary = {"+":add,"-":sub,"*":mul,"/":div}
result = dictionary.get(choice)(x,y)
print(result)
