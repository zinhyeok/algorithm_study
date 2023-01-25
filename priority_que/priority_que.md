# priority que(우선순위 큐)
큐와 다르게 값을 꺼낼 때 우선순위가 가장 높은 값을 제거하는 자료구조

값을 받을 때 동시에 정렬을 하는 알고리즘을 내부적으로 가지고 있음 

collentions 모듈을 통해 제공됨, heapq 모듈을 통해 구현되어 있음 

## heap이란? 
<img width="500" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20221220165711/MinHeapAndMaxHeap1.png">

완전 이진트리로 만들어진 자료구졸, 부모 노드의 값이 자식노드의 값보다 항상 크거나(max-heap) 작은(min-heap) 자료구조 

python에서는 heapq로 min heap을 제공하고 있음 

heapq 모듈에서는 list를 인자로 넘겨 heapq모듈을 사용해야하기에 빈 리스트를 우선 만들어야함 

- heappush(): heap에 원소 추가 O(logn)
```python 
from heapq import heappush
heap = []
heappush(heap, 4)
heappush(heap, 1)
heappush(heap, 7)
heappush(heap, 3)
print(heap)
>>> [1, 3, 7, 4]
```

-heappop():원소를 삭제 O(logn)
```python
from heapq import heappop

print(heappop(heap))
print(heap)
>>> 1
>>>[3,4,7]
```

-heapify(): 기존 list를 heap으로 만들기 

## python에서  우선순위 que 구현 및 연산
오름차순으로 구현되어있음

- que 선언
```python
from queue import PriorityQueue
que = PriorityQueue()
que = PriorityQueue(maxsize=10) #que의 최대크기 설정
```

- .put(): 원소 추가 
```python
from queue import PriorityQueue
que = PriorityQueue()
que.put(3)
```

- .get(): 원소 가져오기(최소값부터)
```python
from queue import PriorityQueue
queue = PriorityQueue()
queue.put(4)
queue.put(8)
queue.put(6)
queue.put(10)
queue.put(2)

print(queue.get())  # 2
print(queue.get())  # 4
print(queue.get())  # 6
print(queue.get())  # 8
print(queue.get())  # 10
```

- 정렬 기준 변경(우선순위 부여) : (우선순위, 값)
```python
que.put((3, 'Apple'))
que.put((1, 'Banana'))
que.put((2, 'Cherry'))

print(que.get()[1])  # Banana
print(que.get()[1])  # Cherry
print(que.get()[1])  # Apple
```

-qsize():size 확인
-empty(): 공백 확인, full(): 가득 찼는지 확인
