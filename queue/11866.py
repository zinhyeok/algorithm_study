from collections import deque
N, K = map(int, input().split())
r_que = deque()
ans = []
#make que
for i in range(N):
    r_que.append(i+1)
#delete logic
for _ in range(N):
    #순회 로직 k-1번 움직이기
    for _ in range(K-1):
        r_que.append(r_que.popleft())

    ans.append(r_que.popleft())
#print ans
print("<",end='')
for i in range(len(ans)-1):
    print("{}, ".format(ans[i]), end='')
print(ans[-1], end='')
print(">")