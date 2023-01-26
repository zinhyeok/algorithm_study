from heapq import heappush, heappop
import sys
N = int(input())
min_heap = []
for _ in range(N):
    cmd = int(sys.stdin.readline().strip())
    if cmd == 0:
        try:
            print(heappop(min_heap))
        except:
            print(0)
    else:
        heappush(min_heap, cmd)