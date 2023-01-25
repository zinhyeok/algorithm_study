# queue 큐
- 선입선출, **FIFO(first in first out)** 형태의 자료구조 
- 가장 먼저 들어온 데이터부터 추출 
- 예시: 식당 번호표, 놀이공원 줄 

<img width="500" src="https://blog.kakaocdn.net/dn/bhvAPe/btqHlVqf0RY/Y4oCoA4wUkEpvIkU80i43K/img.png">

## 용어 및 연산
- front: 삭제 연산만 이루어짐, 줄의 맨 앞 
- rear: 삽입 연산만 이루어짐, 줄의 맨 끝 
- enQueue: rear에서 이루어지는 삽입연산
- dnQueue: front에서 이루어지는 삭제 연산 

## python에서의 구현 

### list를 이용한 구현 
```python
queue = []            
queue.append("a") // enqueue 
queue.pop(0) // dequeue 
```
- 스택과 마찬가지로 list로 구현할 수 있으나 성능적으로 좋지 않다(dequeue)
- append(data)의 시간복잡도 : O(1)
- pop(0)의 시간복잡도 : O(N)(.pop()은 O(1)이나, 특정 index에서 pop을 하려면 O(n))

### dequeue를 이용한 구현  
``` python
from collections import deqeue
dq = deque()
dq.append("a") // enqueue
dq.popleft() // dequeue
```
- 보통 deque를 사용해 구현
- append(data)의 시간복잡도 : O(1)
- popleft()의 시간복잡도 : O(1)
