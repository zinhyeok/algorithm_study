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
