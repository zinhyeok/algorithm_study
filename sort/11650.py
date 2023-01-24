import sys
n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int ,sys.stdin.readline().strip().split())))

lst.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    print(lst[i][0], end=" ")
    print(lst[i][1])