import sys
N, M = map(int, input().split())
board = []
result = []

for i in range(N):
    board.append(sys.stdin.readline().strip())

for i in range(N - 7):
    for j in range(M - 7):
        #시작지점이 B,W에 따라 count 변화, draw1이 시작점이 B인 경우
        draw1 = 0
        draw2 = 0
        # i,j부터 8*8 보드순회
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                # B W B W 일때 B가 아니면 draw1추가
                # a+b %2가 핵심
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        draw1 += 1
                    if board[a][b] != 'W':
                        draw2 += 1
                else:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 1

        result.append(draw1)
        result.append(draw2)

print(min(result))



