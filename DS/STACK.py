#->stack empty or not
#->push (insert)
#->pop (remove)
def isEmpty(stack):
    if stack==[]:
        return True
    else:
        return False
def push(stack,value):
    stack.append(value)
    top = len(stack)-1

def pop(stack):
    if (isEmpty(stack)==True):
        return "UnderFlow Error"
    else:
        value = stack.pop()
        if len(stack)==0:
            top = None
        else:
            top = len(stack)-1
        return value

def peek(stack):
    if (isEmpty(stack)==True):
        return "Underflow"
    else:
        top=len(stack)-1
        return stack[top]

def showStack(stack):
    if (isEmpty(stack)==True):
        return "stack Empty"
    else:
        top = len(stack)-1
        print(stack[top],"<--top")
        for item in range(top-1,-1,-1):
            print(stack[item])
    

Stack = []
top = None

while True:
    print("*********STACK OPERATIONS**********")
    print("Press 1 to push :")
    print("Press 2 to pop :")
    print("Press 3 to peek :")
    print("Press 4 to print stack :")
    print("Press 5 to quit :")
    choice = int(input("Enter Choice"))
    if choice==1:
        value = int(input("Enter value : "))
        push(Stack,value)
    elif choice==2:
        value=pop(Stack)
        if value == "Underflow Error":
            print("Stack is EMPTY")
        else:
            print(f"popped Item is {value}")
    elif choice==3:
        value=peek(Stack)
        if value == "Underflow":
            print("Stack is empty")
        else:
            print(f"top element in {Stack} is {value}")
    elif choice==4:
        showStack(Stack)
    elif choice ==5:
        break
    else:
        print("invalid choice")
    
    
    
