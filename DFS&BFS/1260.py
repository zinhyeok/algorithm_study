import sys
import collections
N, M, V = map(int, input().split())
#인접행렬로 만드는게 풀이가 더 쉬움(양방향 그래프)
q_graph = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    q_graph[a][b] = q_graph[b][a] = 1

visit_dfs = [False for i in range(N+1)]
visit_bfs = [False for i in range(N+1)]

def dfs(graph, visit, start):
    visit[start] = True
    print(start, end=" ")
    for i in range(1, N + 1):
            if graph[start][i] == 1 and visit[i] == False:
                dfs(graph, visit, i)



def bfs(graph, visit, start):
    q = collections.deque()
    q.append(start)
    visit[start] = True
    while q:
        x = q.popleft()
        print(x, end=" ")
        for i in range(1, N + 1):
            if visit[i] == False and graph[x][i] == 1:
                visit[i] = True
                q.append(i)

dfs(q_graph, visit_dfs, V)
print("")
bfs(q_graph, visit_bfs, V)