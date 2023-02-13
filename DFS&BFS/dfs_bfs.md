# DFS&BFS
DFS, BFS는 그래프 탐색 알고리즘(graph traversal algorithm)이다. 

## 그래프(graph)란?
그래프는 Node와 edge로 이루어진 비선형 자료구조의 일종이다. 

<img width="400" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbXVuFb%2Fbtrr4xDAOtc%2FYDJkHEjlmXwc9x8KKGfVXk%2Fimg.png">

그래프의 표현법은 크게 2가지 방법이 있는데, 인접행렬(Adjecency matrix)를 이용한 방법과 인접 리스트(Adjecency list)를 이용한 방법이 있다. 

### 1. 인접행렬 
인접행렬은 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식으로, 각 노드를 행과 열에 모두 작성하고, 해당노드들이 연결괴어 있으면 1로 표현한다

방향 그래프와 무방향 그래프인 경우 표현방법에 약간의 차이가 있다. 무방향 그래프의 경우 A-B가 연결되어 있다면 모두에 1을 표시하나, 방향그래프의 경우 A->B인 경우 matrix_A,B에만 표시한다

즉, 열부분이 간선의 시작점이라 생각하면 된다 

<img width="400" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F1hTUj%2Fbtrr2Tz84x0%2FgzQkMr2lqFo0z3B1SKwwkk%2Fimg.png">

```python
graph = [
    [0, 1, 1, 0], 
    [1, 0, 1, 1], 
    [1, 1, 0, 0], 
    [0, 1, 0, 0]
]
```
### 2. 인접 리스트
인접리스트의 경우 각 노드에 연결된 노드의 정보를 차례대로 기록하는 방식, 그림을 참조하면 편하다 

<image width="400" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdtEp7J%2Fbtrr16z87fn%2Feuc9Rjrb7C64IBkXEK81Bk%2Fimg.png">

```python
graph = [[] for _ in range(4)]

# 노드 A
graph[0].append('B')
graph[0].append('C')

# 노드 B
graph[1].append('A')

...

graph = [['B', 'C'], ['A', 'C', 'D'], ['A', 'B'], ['B']]
```
### 각 표현법의 장단점과 해결법
1. 인접행렬

장점: 두 노드의 연결 여부를 바로 알 수 있다, 즉 A-B일때 B에서 역으로 A를 찾아가기도 편하다 

단점: 필요 메모리가 많다 -> 해결방안: Sparse matrix를 이용한다 

2. 인접리스트

장점: 연결된 것들만 기록해서, 메모리 소비가 적다 

단점: 인접행렬과 달리 역으로 찾아가는 경우 느리다 

## DFS(깊이 우선 탐색)

깊이 우선 탐색이라는 이름과 같이, 한 쪽을 깊게 먼저 탐색하고 다시 루트로 돌아가 다른 경로를 탐색한다. 스택 자료구조를 같이 이용한다 

구체적인 동작과정은 다음과 같다.

1. 탐색 시작 노드를 스택에 삽입, 방문 처리 

2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있다면 그 노드를 스택에 넣고 방문처리, 만약 방문하지 않은 인접노드가 없는 경우 스택에서 pop을 통해 노드를 확인 

3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복 

```python
#v는 시작노드 
def dfs(graph, v, visited):
	#현재 노드 방문 처리
	visited[v]=True
	print(v, end=" ")
	
	#현재노드와 연결된 다른 노드를 재귀적으로 방문
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)


graph = [
    [],      # 0
    [2, 3],  # 1 
    [4, 5],  # 2
    [6],     # 3
    [2, 5],  # 4
    [2, 4],  # 5
    [3, 7],  # 6
    [6]      # 7
]

visited = [False] * 8
dfs(graph, 1, visited)
```
## BFS(너비 우선 탐색)
너비 우선탐색이라는 이름에 맞게 그래프의 너비를 탐색한다. BFS는 그래프를 가로로 탐색함, DFS와 다르게 스택이 아닌 큐를 이용해 순서대로 탐색을 한다 

구체적인 동작과정은 다음과 같다 

구체적인 동작 과정:

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리.

2. 큐에서 노드를 꺼내 해당 노드의 방문하지 않은 모든 인접 노드를 모두 큐에 삽입하고 방문 처리.

3. 2번 과정을 더 이상 수행할 수 없을 때까지 반복.

```python 
from collections import deque

graph = [
    [],      # 0
    [2, 3],  # 1 
    [4, 5],  # 2
    [6],     # 3
    [2, 5],  # 4
    [2, 4],  # 5
    [3, 7],  # 6
    [6]      # 7
]

visited = [False] * 8

def bfs(v):
    # 큐 생성 및 큐에 시작 노드 삽입
    q = deque()
    q.append(v)
    # 아직 방문해야 하는 노드가 있다면
    while q:
        # 큐에서 노드를 꺼내서 x에 저장
        x = q.popleft()
        print(x, end=' ')
        # 그래프를 탐색하다가 방문하지 않은 노드가 있다면
        for i in graph[x]:
            if not visited[i]:
                # 큐에 방문하라고 삽입하고 방문 처리
                q.append(i)
                visited[i] = True

bfs(1)
```
## 예시
<image width="400" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FKyzT6%2Fbtrwhy0Uw5m%2FOwBSLoXaQfHtG4ppC1lkDK%2Fimg.png">

위의 예제로 DFS와 BFS를 각각 적용해보자 

### DFS의 경우
 1. 시작노드인 1을 스택에 넣고 방문처리한다 
 2. 인접노드인 2로 간 후 스택에 넣고 방문처리
 3. 인접노드인 4로 가고 스택에 넣고 방문처리
 4. 인접노드인 5로 가고 스택에 넣고 방문처리 
 5. 5에게 방문하지 않은 인접노드가 없기에 스택에서 5제거
 6. 동일하게 4,2에게 방문하지 않은 인접노드가 없기에 스택에서 4,2제거
 7. 1의 인접노드인 3으로 가고 스택에 넣고 방문처리
 8. 3의 인접노드인 6으로 가고 스택에 넣고 방문처리
 9. 6의 인접노드인 7으로 가고 스택에 넣고 방문처리
 10. 7에게 방문하지 않은 인접노드가 없기에 스택에서 제거
 11. 6,3,1에 모두 동일하게 적용, 스택에 남은 문자가 없기에 종료 
 ### BFS의 경우 
  1. 시작노드인 1을 큐에 넣고 방문처리한다 
  2. 1을 큐에서 꺼내고 인접노드인 2,3으로 간 후 큐에 넣고 방문처리
  3. 2를 큐에서 꺼내고, 인접노드인 4,5로 가고 큐에 넣고 방문처리
  4. 3을 큐에서 꺼내고, 인접노드인 6을 큐에 넣고 방문처리 
  5. 큐에서 4를 꺼내고 방문하지 않은 인접노드가 없음으로 무시 
  6. 큐에서 5를 꺼내고 방문하지 않은 인접노드가 없음으로 무시 
  7. 6을 큐에서 꺼내고, 인접노드인 7을 큐에 넣고 방문처리 
  8. 7을 큐에서 꺼내고, 인접노드가 없음으로 무시
  9. 큐에 문자가 없기에 종료 

둘 다 O(n)이나 일반적으로 BFS가 더 빠르게 작동한다고 한다 


## 🎓 참고자료

https://veggie-garden.tistory.com/28
