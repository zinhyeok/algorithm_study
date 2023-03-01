import sys
from collections import deque
import copy
M, N = map(int, input().split())
box = []
for i in range(N):
    box.append((list(map(int , sys.stdin.readline().strip().split()))))

rotten_T = deque()

for r in range(N):
    for c in range(M):
        if box[r][c] == 1:
            rotten_T.append((r,c))
def bfs(box):
    count = 0
    box = box
    dir = [(1,0), (-1,0), (0,1), (0,-1)]
    while rotten_T:
        past_rotten = copy.deepcopy(rotten_T)
        rotten_T.clear()
        while past_rotten:
            r, c = past_rotten.pop()
            for dr in dir:
                nr = r+dr[0]
                nc = c+dr[1]
                if 0<=nr<N and 0<=nc<M:
                    if box[nr][nc] == -1:
                        continue
                    if box[nr][nc] == 0:
                        box[nr][nc] = 1
                        rotten_T.append((nr,nc))
        count += 1
    return count

ans = bfs(box) -1

for r in range(N):
    for c in range(M):
        if box[r][c] == 0:
            ans = -1
            break

print(ans)

#더 깔끔한 풀이
'''
from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)
'''
