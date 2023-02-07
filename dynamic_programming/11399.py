N = int(input())
lst = list(map(int, input().split()))
ans = 0
lst.sort()
#greedy로 문제해결
for i in range(N):
    ans += lst[i]*(N-i)

print(ans)

#다른 풀이
#lst indexing을 푼 사람도 있음
# for x in range(1, n+1):
#     answer += sum(lst[0:x])  # 리스트의 0번째 수부터 x번째 수까지를 더해줍니다.