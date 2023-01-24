import sys
N = int(input())
lst = []
for i in range(N):
    a,b = sys.stdin.readline().strip().split()
    lst.append([int(a),b])

#lst.sort(key= lambda x:x[0])
lst = sorted(lst,key= lambda x:x[0])

for i in lst:
    print(i[0],i[1])