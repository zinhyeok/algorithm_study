from heapq import heappush, heappop
import sys

N = int(input())
max_heap = []
for i in range(N):
    cmd = int(sys.stdin.readline().strip())
    if cmd == 0:
        try:
            tmp = heappop(max_heap)
            print(tmp[1])
        except:
            print("0")
    else:
        heappush(max_heap, (-cmd,cmd))


