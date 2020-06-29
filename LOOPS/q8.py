import math

x =2
series=0
for i in range(4):
    fact = math.factorial(i+1)
    series += ((-x)**i)/fact 

print(series)


