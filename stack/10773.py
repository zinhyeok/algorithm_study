import sys

K = int(input())
lst = []

for _ in range(K):
    cmd = int(sys.stdin.readline().strip())
    if cmd == 0:
        lst.pop()
    else:
        lst.append(cmd)

sum = 0
for i in lst:
    sum = i+sum

print(sum)