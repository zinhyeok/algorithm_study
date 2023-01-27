from collections import deque
N = int(input())
n = list(map(int, input().split()))

deq = deque()
ans = []
#make balloon
for i in range(N):
    deq.append((i+1,n[i]))

for j in range(N):
    bal = deq.popleft()
    ans.append(bal[0])
    num = bal[1]
    #move
    if len(deq) > 0:
        if num > 0:
            for _ in range(num-1):
                deq.append(deq.popleft())
        else:
            for _ in range(abs(num)):
                deq.appendleft(deq.pop())

for i in ans:
    print(i, end=" ")
