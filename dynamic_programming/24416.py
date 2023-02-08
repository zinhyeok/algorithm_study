n = int(input())
# 1,2 ==1인 case
def fib(n):
    f = [0 for i in range(n+1)]
    f[1] = 1
    f[2] = 1
    for idx in range(3, n+1):
        f[idx] = f[idx-2] + f[idx-1]
    return f[n]
count = fib(n)
#count = fib(n)인 이유: fib(1)=count(1), fib(2)=count(2) -> fib(n)=count인가? 귀납적 증명법으로 증명가능
#https://freshmath.tistory.com/6

print(count,n-2)