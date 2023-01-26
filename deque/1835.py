from collections import deque

N = int(input())
deq = deque()
for i in range(N,0,-1):
    deq.appendleft(i)
    for j in range(i):
        tmp = deq.pop()
        deq.appendleft(tmp)

for i in deq:
    print(i, end=" ")