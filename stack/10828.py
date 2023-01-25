import sys
N = int(input())

class stack:
    def __init__(self):
        self.lst = []

    def size(self):
        return len(self.lst)

    def empty(self):
        if self.size() > 0:
            return 0
        else:
            return 1

    def push(self,x):
        self.lst.append(x)

    def pop(self):
        if self.empty() != 1:
            return self.lst.pop()
        else:
            return -1

    def top(self):
        if self.empty() != 1:
            return self.lst[-1]
        else:
            return -1

stk = stack()

for i in range(N):
    cmd = sys.stdin.readline().strip().split()
    # print(stk.lst)
    if cmd[0] == "push":
        stk.push(cmd[1])
    elif cmd[0] == "pop":
        print(stk.pop())
    elif cmd[0] == "size":
        print(stk.size())
    elif cmd[0] == "empty":
        print(stk.empty())
    elif cmd[0] == "top":
        print(stk.top())
    else:
        pass





