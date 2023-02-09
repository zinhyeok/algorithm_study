import sys

#greedy algorithm
#lst, idx -> lst에서 해당 idx 제외하고 min인거 색칠하기 가격은 global 변수에 더하기
#문제에서 최소값을 찾을때 그냥 최소값이 아닌 누적최솟값을 찾아야한다!!, 그냥 최솟값 계산시 예제 4에 걸림

N = int(input())
RGB = []
for i in range(N):
    RGB.append(list(map(int, sys.stdin.readline().strip().split())))
for i in range(1,N):
    #빨간집의 i번째 선택시 cost는 RGB[i][0]+ 이전에서 올수 있는 최소값은 G,B에서 온다
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0]
    RGB[i][1] = min(RGB[i - 1][0], RGB[i - 1][2]) + RGB[i][1]
    RGB[i][2] = min(RGB[i - 1][0], RGB[i - 1][1]) + RGB[i][2]

print(min(RGB[N-1]))