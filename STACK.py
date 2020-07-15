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

Stack = []
top = None

while True:
    print("*********STACK OPERATIONS**********")
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
    
    
    
