# deque (덱)
deque(double ended queue), 덱이란 양쪽에서 삽입과 삭제가 가능한 구조로 스택과 큐의 연산을 모두 지원한다

**python collenctions 모듈에서 deque를 제공**

<img width="500" src="https://velog.velcdn.com/images%2Ffalling_star3%2Fpost%2F10df11e7-f1b7-4e8d-ae57-7224ab2af1fa%2F2.JPG">

## 연산
좌우에서 삭제/추가를 하는 연산들 제공
- append(): 오른쪽에서 데이터를 삽입
- pop(): 오른쪽에서 데이터를 삭제 
- appendleft(): 왼쪽에서 데이터를 삽입
- popleft(): 왼쪽에서 데이터를 삭제

## python에서 구현 
```python 
from collections import deque

queue = deque()
queue.append(1)
>>[1]
queue.appendleft(2)
>>[2,1]
queue.append(3)
>>[2,1,3]
queue.pop()
>>[2,1]
queue.popleft()
>>[1]
queue.append(5)
>>[1,5]
print(queue)

# 결과
deque([1, 5])
```

## list와 비교
python의 list는 이름과 다르게 고정된 사이즈의 메모리를 갖는 동적배열형태이다
- pop(0) vs popleft() 

N개의 원소를 가진 list에서 pop(0)를 하게 되면 list의 첫번째 원소를 삭제하고 난 뒤에 N-1개의 요소들이 모두 shift하며 앞으로 한칸씩 이동해야한다

따라서 list를 이용해 que의 dequeue를 구현하면 O(n)의 시간복잡도를 가짐으로 duqueue를 이용해 queue를 구현한다 
