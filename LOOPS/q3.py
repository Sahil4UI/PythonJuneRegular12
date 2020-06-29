#Sum of Digits of a Number
# 112 -> 1+1+2=4
number = int(input("Input a Number : "))
sum=0
temp = number

for i in range(len(str(number))):
    rem = number %10
    sum += rem**3
    number = number//10

if (temp == sum):
    print("Number is Armstrong")
else:
    print("Number is Not Armstrong")



#check wether number is Armstrong or Not
# 153 => 1^3+5^3+3^3 = 1 + 125+ 27 = 153 