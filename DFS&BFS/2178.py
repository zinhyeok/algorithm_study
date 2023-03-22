import sys
from collections import deque
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append((list(map(int ,sys.stdin.readline().strip()))))

global count
count = 1
def bfs(x,y):
    que = deque()
    que.append((x,y))
    dr = [(-1,0), (1,0), (0,-1), (0,1)]
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dr[i][0]
            ny = y + dr[i][1]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    que.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1

    return graph[N-1][M-1]


print(bfs(0,0))

