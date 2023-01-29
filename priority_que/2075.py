import sys
N = int(input())
lst = []
#메모리 제한
for i in range(N):
    lst = lst + list(map(int,sys.stdin.readline().strip().split()))
    lst.sort(reverse=True)
    lst = lst[0:N]

print(lst[N-1])

# 다른 풀이 heap이용, heap은 기본적으로 min heap이기에 크기를 n으로 유지하면서 최솟값과 계속 비교
# heap의 길이가 n보다 크면 heappop(가장 작은 원소를 pop)해줘서 heap길이 조절
# (문제에서 n번째 큰 수를 원하기 때문에 n밖의 숫자들 버려도 된다)
'''
import sys
import heapq

N = int(input())
heap= []

for _ in range(N):
    line = map(int, sys.stdin.readline().split())
    for x in line:
        heapq.heappush(arr, x)
        if (len(arr)>N):
            heapq.heappop(heap)

print(heapq.heappop(heap))
'''