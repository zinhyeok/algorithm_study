N = int(input())
ans = 0
for i in range(N):
    sum = i
    str_i = str(i)
    for j in str_i:
        sum += int(j)
    if N == sum:
        ans = i
        break

print(ans)