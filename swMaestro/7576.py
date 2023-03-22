import sys
from collections import deque
N, M = map(int, input().split())

box = []
for i in range(M):
    box.append(list(map(int, sys.stdin.readline().strip().split())))

#모든 행렬을 돌면서 토마토가 있는 곳을 확인한다(1)
#해당 위치 주변(bfs)로 돌면서 0이면 1로 바꾼다
#다시 for문을 돌린다

print(box)
que = deque()

for c in range(N):
    for r in range(M):
        if box[r][c] == 1:
            que.append([r,c])
def bfs():
    dirs = [[0,1], [1,0], [0,-1], [-1,0]]
    while que:
        r,c = que.popleft()
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if 0<=nr<M and 0<=nc<N:
                if box[nr][nc] == -1:
                    continue
                if box[nr][nc] == 0:
                    que.append([nr,nc])
                    box[nr][nc] = box[r][c] + 1

bfs()
ans = max(max(box))-1

for r in range(M):
    for c in range(N):
        if box[r][c] == 0:
            ans = -1
            break


print(ans)
