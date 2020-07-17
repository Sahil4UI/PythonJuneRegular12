def isEmpty(q):
    if q == []:
        return True
    else:
        return False
def enqueue(q,value):
    q.append(value)
    if(len(q)==1):
        front=rear=0
    else:
        rear=len(q)-1
def dequeue(q):
    if isEmpty(q) == True:
        return "underflow"
    else:
        value=q.pop(0)
    if len(q)==0:
        front=rear=None
    return value

Queue=[]

while True:
    print("""***********Queue Operation Menu ************
Press 1 for EnQueue
Press 2 for DeQueue
""")
    choice = int(input("enter choice: "))
    if choice ==1:
        value =int(input("Enter Element in Queue : "))
        enqueue(Queue,value)
    elif choice ==2:
        value = dequeue(Queue)
        if value == "underflow":
            print("Queue is Empty")
        else:
            print("Element removed is :",value)


        
    
