import sys
N, M = map(int, input().split())
lst = []
for i in range(N):
    lst.append([j for j in sys.stdin.readline().strip()])

#정사각형의 최대 크기는 N
#특정숫자가 N index 차이나는가?를 찾으면 됨
#특정숫자를 행기준으로 먼저 찾고 그 특정숫자의 index에서 i만큼 늘려서 찾으면 됨
#ans = 1추가하는거 잊지 말기!! -> 빈리스트면 max값 반환을 못함 
ans = [1]

for i in range(N):
    for j in range(M):
        for k in range(N, 0, -1):
            try:
                if lst[i][j] == lst[i][j+k] and lst[i][j] == lst[i+k][j] and lst[i][j] == lst[i+k][j+k]:
                    ans.append(k+1)
            except:
                pass
max_length = int(max(ans))
print(max_length*max_length)