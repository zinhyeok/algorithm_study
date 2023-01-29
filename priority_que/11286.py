from heapq import heappush, heappop
import sys
abs_min_heap = []
N = int(input())

for _ in range(N):
    cmd = int(sys.stdin.readline().strip())
    if cmd == 0:
        try:
            print(heappop((abs_min_heap))[1])
        except:
            print(0)
    else:
        heappush(abs_min_heap, (abs(cmd), cmd))
