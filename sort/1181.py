import sys
N = int(input())
lst = []
se = set()
for i in range(N):
    se.add(sys.stdin.readline().strip())
lst = list(se)
lst.sort(key= lambda x: (len(x), x))

for i in lst:
    print(i)
#set() -> list를 set으로 변경 가능, list()는 반대로, set 선언시 set()으로 선언