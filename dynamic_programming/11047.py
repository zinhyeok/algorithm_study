import sys

N, K = map(int, input().split())
lst_coin = []
ans = 0

for i in range(N):
    lst_coin.append(int(sys.stdin.readline().strip()))

lst_coin.sort(reverse=True)

for coin in lst_coin:
    if K >= coin:
        ans += K//coin
        K = K%coin

print(ans)

