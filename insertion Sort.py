list1 = [9,3,0,4,1]

for i in range(0,len(list1)-1):
    for j in range(i+1,len(list1)):
        if list1[i] > list1[j]:
            list1[j],list1[i]=list1[i],list1[j]

print(list1)
        
        
            
