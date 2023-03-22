import sys
from itertools import permutations
#접근 1
#permutaion?
# 1로 나눌 수 있을 때 까지 나눈다, 1을 2개 합하면 2가 된다, 1을 3개 합하면 3이 된다,
def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sol(n-1)+sol(n-2)+sol(n-3)

T = int(input())

for i in range(T):
    print(sol(int(sys.stdin.readline().strip())))


