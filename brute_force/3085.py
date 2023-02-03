import sys
N = int(input())
lst = []
for _ in range(N):
    lst.append([i for i in sys.stdin.readline().strip()])

maxCount = 0

#배열의 행 검사
def width():
    global maxCount
    for i in range(N):
        countRow = 1
        for j in range(N-1):
            if lst[i][j] == lst[i][j+1]:
                countRow += 1
                maxCount = max(maxCount, countRow)
            else:
                countRow = 1

#배열의 열 검사
def height():
    global maxCount
    for j in range(N):
        countCol = 1
        for i in range(N-1):
            if lst[i][j] == lst[i+1][j]:
                countCol += 1
                maxCount = max(maxCount, countCol)
            else:
                countCol = 1

for i in range(N):
    for j in range(N - 1):
        # 만약 입력 받은 배열의 행의 원소가 다르다면
        if lst[i][j] != lst[i][j + 1]:
            lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]
            width()
            height()
            lst[i][j + 1], lst[i][j] = lst[i][j], lst[i][j + 1]
        # 만약 입력 받은 배열의 열의 원소가 다르다면
        if lst[j][i] != lst[j + 1][i]:
            lst[j][i], lst[j + 1][i] = lst[j + 1][i], lst[j][i]
            width()
            height()
            lst[j + 1][i], lst[j][i] = lst[j][i], lst[j + 1][i]

print(maxCount)