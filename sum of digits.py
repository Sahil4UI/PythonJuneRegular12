def s_o_d(n):
    if n==0:
        return 0
    return n%10 + s_o_d(n//10)

solution=s_o_d(12345)
print(solution)
