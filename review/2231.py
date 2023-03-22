#216 -> 198+1+9+8
N = int(input())
ans = 0
#특정숫자 N이 주어졌을 때 탐색범위는 216 -> 198 + 1+9+8 -> 3개 합은 최대 9*3->27 216-27 뺀거부터 숫자하나씩 늘리면서 찾기?
#100이면 91 -> 91 + 9 + 1
try:
    for i in range(N-9*len(str(N)), N):
        sum = i
        str_i = str(i)
        for j in str_i:
            sum += int(j)
        if N==sum:
            ans = i
            break
except:
    ans = 0
print(ans)

