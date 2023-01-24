import sys
N = int(input())
n_set = set(sys.stdin.readline().strip().split())

M = int(input())
m_lst = sys.stdin.readline().strip().split()
for i in range(M):
    if m_lst[i] in n_set:
        m_lst[i] = 1
    else:
        m_lst[i] = 0
for i in range(M):
    print(m_lst[i], end=" ")

#set의 경우 시간복잡도 O(1)을 가짐 -> hash테이블을 이용했기 때문