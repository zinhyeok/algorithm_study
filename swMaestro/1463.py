from collections import deque
# if x%3==0: x/3, if x%2==0: x/2, else -1 -> make 1
#단순히 if else로 빼면 안될듯..? -> 큰 숫자로 먼저 나누는 것이 가장 중요
#풀이법은 크게 3가지
#DP를 이용한 문제인데, dp인지 아닌지 판단하는 방법은 그리디랑 비슷한 느낌
#이번 문제 또한 10을 1로 만드는 것은 10 -> 9(그럼 9에서 1로가는 방법은?) 이런 느낌
#so1 1dp bottom up
def sol1():
    x = int(input())
    d = [0]*(x+1)
    #1은 어차피 0번, 0은 고려 불가
    for i in range(2, x+1):
        d[i] = d[i - 1] + 1
        #4을 예시로 하자, 그러면 4는 기본적으로 3으로 가려면 어차피 1번 빼야함
        #3을 예시로 하자, 3은 기본적으로 2로 갈 수도 있지만, 3으로 나눌수도 있음 -> 따라서 두 케이스를 비교 가능, +1을 하는건 나누는 행위 자체가 횟수를 한번 사용
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
    print(d[x])
#Top-Down 풀이
def sol2():
    x = int(input())
    dp = {1: 0}
    def rec(n):
        if n in dp.keys():
            return dp[n]
        if (n % 3 == 0) and (n % 2 == 0):
            dp[n] = min(rec(n // 3) + 1, rec(n // 2) + 1)
        elif n % 3 == 0:
            dp[n] = min(rec(n // 3) + 1, rec(n - 1) + 1)
        elif n % 2 == 0:
            dp[n] = min(rec(n // 2) + 1, rec(n - 1) + 1)
        else:
            dp[n] = rec(n - 1) + 1
        return dp[n]
    print(rec(x))
#잠깐! top-down, bottom up의 차이는?? top-down의 경우 재귀를 이용, 점화식을 이해하기 편하다
# bottom-up은 시간과 메모리적 이점이 있음

def sol3():
    x = int(input())
    Q = deque([x])
    visited = [0] * (x + 1)
    #visited는 횟수를 저장하는 자료구조
    #c는 해당숫자
    while Q:
        c = Q.popleft()
        if c == 1:
            break
        if c % 3 == 0 and visited[c // 3] == 0:
            Q.append(c // 3)
            visited[c // 3] = visited[c] + 1
        if c % 2 == 0 and visited[c // 2] == 0:
            Q.append(c // 2)
            visited[c // 2] = visited[c] + 1
        if visited[c - 1] == 0:
            Q.append(c - 1)
            visited[c - 1] = visited[c] + 1
    print(visited[1])

sol1()