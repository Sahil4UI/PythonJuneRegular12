# Series ->
# 1/1! +2/2!+------

number = 10
series = 0
factorial = 1
for i in range(1,number+1):
    factorial *= i
    series = series + i/factorial

print(series)
