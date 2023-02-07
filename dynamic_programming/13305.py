N = int(input())
street_lst = list(map(int, input().split()))
oil_lst = list(map(int, input().split()))
ans = 0


#bottom-up방식
min_oil = oil_lst[0]
oil_lst = oil_lst[1:]

for i in range(N-1):
    ans += min_oil * street_lst[i]

    if min_oil > oil_lst[i]:
        min_oil = oil_lst[i]


print(ans)