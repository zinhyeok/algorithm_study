import sys
num = sys.stdin.readline().strip()
lst = []
for i in range(len(num)):
    lst.append(int((num[i])))
lst.sort(reverse=True)
for i in range(len(num)):
    print(lst[i], end="")
