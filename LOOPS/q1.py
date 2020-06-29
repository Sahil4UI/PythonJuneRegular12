#check wether traingle is equilateral , isoceles or scalene
a = int(input("Enter first side of Traingle"))
b = int(input("Enter second side of Traingle"))
c = int(input("Enter Third side of Traingle"))

if ((a+b > c) and (b+c>a) and (a+c>b)):
    if (a == b == c):
        print("Traingle is Equilateral")
    elif (a == b) or (a==c) or (b==c):
        print("Traingle is Isoceles")
    else:
        print("Traingle is Scalene")
else:
    print("Invalid sides for building a Traingle")

