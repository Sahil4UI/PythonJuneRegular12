'''a=0
for i in range(1,5):
    for j in range(i):
        a+=1
        print(a,end='')
    print()
'''
'''
homework
1-loop - *
1-loop - \n
1-lopp - spacing
      *
     ***
    *****
   *******
  *********
'''
#for i in range(7):
#    print(' '*(7-i)+'*'*(2*i+1))
#alternative
'''
for i in range(7):
    for j in range(7-i):
        print(' ',end='')
    for k in range(2*i+1):
        print('*',end='')
    print()
'''


'''
      1
     2 3
    4 5 6
   7 8 9 10
  
'''
a = 0
for i in range(1,5):
    for j in range(5-i):
        print(' ',end='')
    for k in range(i):
        a+=1
        print(a,end=' ')
    print()


#HOME WORK
'''
A
AB
ABC
ABCD
ABCDE


A
BC
DEF
GHIJ
KLMNO

A
BB
CCC
DDDD
EEEEE
'''

    


