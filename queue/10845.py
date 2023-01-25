import sys
from collections import deque
que = deque()
N = int(input())
for i in range(N):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0] == "push":
        que.append(cmd[1])
    elif cmd[0] == "pop":
        try:
            print(que.popleft())
        except:
            print(-1)
    elif cmd[0] == "size":
        print(len(que))
    elif cmd[0] == "empty":
        if len(que)==0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        try:
            front = que.popleft()
            print(front)
            que.appendleft(front)
        except:
            print(-1)
    elif cmd[0] == "back":
        try:
            back = que.pop()
            print(back)
            que.append(back)
        except:
            print(-1)
    else:
        pass