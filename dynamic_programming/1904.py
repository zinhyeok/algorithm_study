
#n=1 -> 1 n=2 00, 11 -> 2  n=3 ->  111, 100, 001 -> n=4 ( [00]11, [00]00, [1]001, [1]100, [1]111)
#d[n] = n-1 + n-2
n = int(input())
dp = {}
dp[1] = 1
dp[2] = 2

for k in range(3,n+1):
    dp[k] = (dp[k-1]+ dp[k-2])%15746
print(dp[n])


'''
두번째 풀이 시간초과 -> 경우의 수 이용, factorial 함수 이용
# 경우의 수 문제 중복이 있는 경우의 수
import math
N = int(input())
max_num_00 = N//2
ans = 0
for i in range(max_num_00+1):
    ans += math.factorial(N-i)/(math.factorial(i)*math.factorial(N-(i*2)))

ans = ans%15746
print(int(ans))
'''
# N=5  _____ -> 00 00 1 /  00 1 1 1 1 / 11111 -> 순열 만들기
# 00의 최대개수 N//2, 1의 개수는 N-00의 개수 *2, 전체 순열의 크기 -> tile의 개수
'''
from itertools import combinations, permutations
첫번째 풀이 -> 시간초과 
max_num_00 = N//2
tiles = []
ans = 0

for i in range(max_num_00+1):
    tiles.extend(["00" for _ in range(i)])
    tiles.extend(["1" for _ in range(N-(i*2))])
    ans += len(set(permutations(tiles,len(tiles))))
    tiles.clear()
ans = ans%15746
print(ans)
'''
