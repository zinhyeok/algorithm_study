<<<<<<< HEAD
import sys
from collections import deque
N, M = map(int,input().split())
maze = []
for i in range(N):
    maze.append(list(map(int, sys.stdin.readline().strip())))

def bfs(x,y,maze):
    que = deque()
    que.append((x,y))
    diretions = [(1,0),(-1,0),(0,1),(0,-1)]
    while que:
        x, y = que.popleft()
        for diretion in diretions:
            nx = x + diretion[0]
            ny = y + diretion[1]
            if 0<=nx<N and 0<=ny<M:
                if maze[nx][ny] == 0:
                    continue
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    que.append((nx, ny))

    return maze[N-1][M-1]


print(bfs(0,0,maze))
=======
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
>>>>>>> 4259e4250a44402e6ff5acb321d4a18cd02b4272
