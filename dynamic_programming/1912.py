
n = int(input())
lst = list(map(int,input().split()))
# 1 2 3 3 4 5 6  -100 10 -23
ans = [0 for i in range(n)]
ans[0] = lst[0]
for i in range(1,n):
    ans[i] = max(lst[i], ans[i-1] + lst[i])

print(max(ans))

#풀이 i번째 ans는 0번째를 제외하고는 1번째부터는 lst[1], 그전까지의 합 + 새로운수 더하기의 max비교후 값 넣기 -> 값이 증가하면 계속 추가
#그 중 max값을 뽑으면 누적합의 최대가 나옴