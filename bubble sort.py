list1 = [5,6,0,3,9,1]

for i in range(len(list1)):
    for j in range(0,len(list1)-i-1):
        if list1[j] > list1[j+1]:
            list1[j],list1[j+1] = list1[j+1],list1[j]

print(list1)
            
