import sys
N = int(input())
lst = []
lst = list(map(int, sys.stdin.readline().strip().split()))
sort_lst = sorted(set(lst))

#new_lst = [sort_lst.index(i) for i in lst]

#for i in new_lst:
#    print(i, end=" ")
#.index O(n)의 시간복잡도를 가지는 함수 -> 시간초과
#set으로 겹치는 원소 제거 + dict로 key-value탐색 이용 O(1) 시간복잡도로 변형

dic = {sort_lst[i]: i for i in range(len(sort_lst))}
for i in lst:
    print(dic.get(i), end=" ")