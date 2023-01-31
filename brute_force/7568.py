import sys
N = int(input())
lst = []
ans = []
for i in range(N):
    a, b = sys.stdin.readline().strip().split()
    lst.append([int(a), int(b)])


for i in range(N):
    K = 0
    for j in range(N):
        if i != j:
            if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
                    K += 1
    ans.append(K+1)

for i in ans:
    print(i, end= " ")