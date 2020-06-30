#find the Largest Element from the List
list1=[99,100,10000,-1,-2,9000,0,2,30]
maximum = list1[0]

for i in range(0,len(list1)):
    if(maximum < list1[i]):
        maximum = list1[i]

'''for item in list1:
    if(maximum < item):
        maximum = item
'''
print(maximum)

