import sys

n = int(input())
stair = []
for i in range(n):
    stair.append(int(sys.stdin.readline().strip()))

'''
계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다. -> 2, 1, 1 ok 1, 1, 1,은 불가 
마지막 도착 계단은 반드시 밟아야 한다
'''
#greedy로 접근?
#예: 1 3 5 7 일때 -> 7 5 1, 7 3 1, 7 5 .. -> 1 3 5 7 9 -> 9, 7... 9, 5...
#bfs??
def greedy_stair(lst):
    n = len(lst)
    dp = [0]*(n+1)
    dp[1] = lst[0]
    dp[2] = lst[1] + lst[0]
    #3번째 계간부터 1,2,3은 불가 -> 3, 2, 0 or 3, 1, 0
    #dp[5] = 5 -> 4 2 or 5 -> 3 2 or 5 -> 3, 1 문제는 5, 4, 3은 불가

    for i in range(3,n+1):
        dp[i] = lst[i - 1] + max(lst[i - 2]+dp[i-3], dp[i - 2])
    print(dp[-1])
if len(stair) <= 2:
    print(sum(stair))
else:
    greedy_stair(stair)