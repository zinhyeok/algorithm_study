import sys
N, K = map(int, input().split())
lst_coin = []
ans_lst = []
ans = 0

for i in range(N):
    lst_coin.append(int(sys.stdin.readline().strip()))

while True:
    if K >= lst_coin[-1]:
        K -= lst_coin[-1]
        ans_lst.append(lst_coin[-1])
        ans += 1
    else:
        lst_coin.pop()
    if K==0:
        break

print(ans)