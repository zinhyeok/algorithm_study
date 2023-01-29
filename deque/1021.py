from collections import deque
que = deque()
ans = 0
N, M = map(int, input().split())
for i in range(1,N+1):
    que.append(i)

cmd_lst = input().split()

for i in range(M):
    cmd = int(cmd_lst[i])
    while True:
        if cmd == que[0]:
            que.popleft()
            break
        #case 1: 1 2 3 4 5 6... 10 11 -> 2를 뽑아야한다
        #elif cmd < que[len(que)//2] :
        #-> 시간초과 & index 받는게 더 정확함 한번 뽑고 난 뒤에는 정렬이 보장되지 않음
        elif que.index(cmd) < len(que)/2:
            tmp = que.popleft()
            que.append(tmp)
            ans +=1
        # case 2: 1 2 3 4 5 6... 10 11 -> 10을 뽑아야한다
        else:
            tmp = que.pop()
            que.appendleft(tmp)
            ans+=1

print(ans)