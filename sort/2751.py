import sys
N = int(input())
lst = []
for i in range(N):
    lst.append(int(sys.stdin.readline().strip()))
lst.sort()

for i in range(N):
    print(lst[i])