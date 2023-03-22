import sys
from collections import deque
N = int(input())
home_lst = []
for i in range(N):
    home_lst.append(list(map(int,[i for i in sys.stdin.readline().strip()])))
#주의 바로 map, int처리시 0으로 시작하면 0이 날라감
#bfs 이용, 각 단지를 돌면서 방문한 단지는 -1로 처리하면서 숫자를 센다
# 단지 탐색이 멈추면 값을 ans에 반환하고, 새로운 시작단지를 찾는다(1인 부분을 탐색)

#단지탐색로직, 토마토랑 비슷
def bfs(start_x, start_y, home_lst):
    que = deque()
    dirs = [[0,1], [0,-1], [1,0], [-1,0]]
    que.append([start_x, start_y])
    home_lst[start_x][start_y] = -1
    count = 1
    while que:
        x = que.popleft()
        for i in range(4):
            nx = x[0] + dirs[i][0]
            ny = x[1] + dirs[i][1]
            if 0 <= nx < N and 0<= ny <N and home_lst[nx][ny] == 1:
                home_lst[nx][ny] = -1
                que.append([nx, ny])
                count += 1
    return count

ans = []
for i in range(N):
    for j in range(N):
        if home_lst[i][j] == 1:
            ans.append(bfs(i,j, home_lst))

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])


## 맞음!!! 