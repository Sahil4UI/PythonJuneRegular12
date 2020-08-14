#Exception Handling
#Error
#-syntactical error
#-run time error
#-exception -> exception Handling

a = int(input("Enter number 1 :"))
b = int(input("Enter number 2 :"))

try:
    #list1 = [1,2,3,4]
    #print(list1[100])
    p = a+b
    print("sum=",p)
    q = a-b
    print("sub=",q)
    r = a*b
    print("mul=",r)
    s = a/b
    print("div=",s)
    

#except BaseException as be:
#    print(be)

except ZeroDivisionError as a1:
    print(a1)

except IndexError as a2:
    print(a2)
    
finally :
    print("Hello")
    

    
