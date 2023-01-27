import sys
n = int(input())
stack = []
flag = []
start = 1
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    while start <= num:
        stack.append(start)
        flag.append("+")
        start += 1
    if stack[-1] == num:
        stack.pop()
        flag.append("-")
    else:
        flag.clear()
        flag.append("NO")
        break

for i in flag:
    print(i)