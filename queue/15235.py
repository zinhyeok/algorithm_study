N = int(input())
lst = list(map(int, input().split()))
ans = [0 for i in range(N)]
i = 0
count = 1
while True:
    if lst[i] > 0:
        lst[i] += -1
        ans[i] = count
        count += 1
    else:
        pass
    i += 1
    if i == N:
        i=0
    if lst == [0 for i in range(N)]:
        break

for i in ans:
    print(i, end=" ")