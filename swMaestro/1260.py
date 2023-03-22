import sys
from collections import deque
N, M, V = map(int, input().split())

matrix = [[0]*(N+1) for _ in range(N+1)]
# 1 2 -> 1 2 0인 부분은 비우고 시작
for _ in range(M):
    r, c = map(int, sys.stdin.readline().strip().split())
    matrix[r][c] = matrix[c][r] = 1

def bfs(tree, start):
    que = deque()
    que.append(start)
    visited = [0]*(N+1)
    visited[start] = 1
    while que:
        x = que.popleft()
        print(x, end=" ")
        for i in range(1,N+1):
            if tree[x][i]==1 and visited[i]==0:
                que.append(i)
                visited[i] = 1

def dfs(tree, start):
    stack = []
    stack.append(start)
    visited = [0]*(N+1)
    while stack:
        x = stack.pop()
        if visited[x]==0:
            print(x, end=" ")
            visited[x] = 1
        for i in range(len(tree[x])-1, -1, -1):
            if tree[x][i]==1 and visited[i]==0:
                stack.append(i)

dfs(matrix, V)
print()
bfs(matrix, V)

