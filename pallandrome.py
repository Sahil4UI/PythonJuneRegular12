def checkPal(string,start,end):
    if(start == end):
        return True
    if(string[start]!=string[end]):
        return False
    if (start < end+1):
        return checkPal(string,start+1,end-1)
    
    return True



a = ""
i=0
j=len(a)-1
if (len(a) ==0):
    print("String is Empty")
else:
    print(checkPal(a,i,j))
