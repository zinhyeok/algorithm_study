import sys

N = int(input())
n_lst = list(map(int, sys.stdin.readline().split()))
M = int(input())
m_lst = list(map(int, sys.stdin.readline().split()))

n_lst.sort() #binary search need sorted array

def binary_search(data, target, start, end):
    if start > end:
        return None

    mid = (start+end)//2

    if target == data[mid]:
        return data[mid]
    elif data[mid] > target:
        #왼쪽 탐색
        return binary_search(data, target, start, mid-1)
    elif data[mid] < target:
        #오른쪽 탐색
        return binary_search(data,target,mid+1,end)
    else:
        return None


for i in range(M):
    if binary_search(n_lst, m_lst[i], 0, N - 1) != None:
        print(1, end=' ')
    else:
        print(0, end=' ')