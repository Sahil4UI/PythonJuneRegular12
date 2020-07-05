#OPR-OPERATOR
def Calc(a,b,opr):
    return a+opr+b
x = input("Enter the first Number: ")
y = input("Enter the second Number: ")

print('''
Press + for addition
Press - for subtraction
Press * for Multiplication
Press / for Division
''')

choice=input("Enter Choice: ")
result = Calc(x,y,choice)
print(eval(result))
