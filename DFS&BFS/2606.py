import sys

N = int(input())
E = int(input())
global ans
ans = 0
graph = [[0 for i in range(N+1)] for j in range(N+1)]

for i in range(E):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = graph[b][a] = 1

visit = [0 for i in range(N+1)]

def dfs(graph, start, visit):
   visit[start] = 1
   global ans
   # print(start, end= " ")
   for i in range(N+1):
       if graph[start][i] == 1 and visit[i] == 0:
           ans += 1
           dfs(graph, i, visit)

dfs(graph, 1, visit)
print(ans)