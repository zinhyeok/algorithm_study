import sys

N = int(input())
home_lst = []
for _ in range(N):
    home_lst.append(list(map(int, sys.stdin.readline().strip().split())))

def sol(home_lst):
    for i in range(1, len(home_lst)):
        #순서대로 RGB, i번째집의 누적을 업데이트
        home_lst[i][0] = home_lst[i][0] + min(home_lst[i-1][1], home_lst[i-1][2])
        home_lst[i][1] = home_lst[i][1] + min(home_lst[i-1][0], home_lst[i-1][2])
        home_lst[i][2] = home_lst[i][2] + min(home_lst[i-1][0], home_lst[i-1][1])
    return min(home_lst[len(home_lst)-1])

print(sol(home_lst))
#RGB 비용
#색이 연속되게 겹치면 안됨
