# 1 2 3 4 5 6 7 8 9 10
#10-1
'''def my123(x):
    if x==0:
        return
    print(x)
    my123(x-1)'''


#my123(10)
#1234554321
def my123(x):
    if x>5:
        return
    print(x)
    my123(x+1)
    print(x)
    
my123(1)

