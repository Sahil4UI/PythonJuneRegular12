#Binary Search
def binarySearchAlgo(data,value):
    left =0
    right = len(list1)-1
    while left <=right:
        mid = (left+right)//2
        if (value == list1[mid]):
            return True
        elif value < list1[mid]:
            right = mid-1
        else:
            left = mid+1

list1 = [-1,1,3,4,5,6,7,8,15,17,20,90,1000,10000]
value=int(input("Enter Value : "))
print(binarySearchAlgo(list1,value))

