import sys
n = int(input())
tree = []

for _ in range(n):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))

#bfs로 접근 -> 틀린 풀이(500이 넘는 삼각형이라 문제 있음)
#dp문제 -> 최종 max를 찾으면 된다
dp = [[0]*(n+1) for _ in range(n+1)]

dp[0][0] = tree[0][0]

for row in range(1, n):
    for col in range(len(tree[row])):
        if col == 0:
            dp[row][col] = dp[row - 1][col] + tree[row][col]
        elif col == len(tree[row])-1:
            dp[row][col] = dp[row - 1][col - 1] + tree[row][col]
        else:
            dp[row][col] = tree[row][col] + max(dp[row - 1][col - 1], dp[row - 1][col])

print(max(dp[n - 1]))

