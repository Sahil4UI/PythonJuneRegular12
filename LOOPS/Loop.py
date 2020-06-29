#check whether no is prime or not?
number = int(input("Enter the Number"))

for i in range(2,number):
    if(number%i ==0):
        print("Number is Not PRime")
        break
else:
    print("Number is Prime")
