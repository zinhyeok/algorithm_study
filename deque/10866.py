import sys
from collections import deque
N = int(input())
deq = deque()
for _ in range(N):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0]=="push_front":
        deq.appendleft(cmd[1])
    elif cmd[0]=="push_back":
        deq.append(cmd[1])
    elif cmd[0] == "pop_front":
        try:
            print(deq.popleft())
        except:
            print("-1")
    elif cmd[0] == "pop_back":
        try:
            print(deq.pop())
        except:
            print("-1")
    elif cmd[0] == "size":
        print(len(deq))
    elif cmd[0] == "empty":
        if(len(deq)==0):
            print("1")
        else:
            print("0")
    elif cmd[0] == "front":
        try:
            tmp = deq.popleft()
            print(tmp)
            deq.appendleft(tmp)
        except:
            print("-1")
    elif cmd[0] == "back":
        try:
            tmp = deq.pop()
            print(tmp)
            deq.append(tmp)
        except:
            print("-1")
    else:
        pass