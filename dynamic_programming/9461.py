import sys
T = int(input())

memo_wave = {}
# memo[6] = 1+2 = memo[1]+memo[5]= memo[n-5]+memo[n-1]

#Top bottom
def wave(n, memo={}):
    if n==0 or n==1 or n==2 or n==3:
        return 1
    elif n==4 or n==5:
        return 2
    elif n in memo:
        return memo[n]
    else:
        memo[n] = wave(n-1,memo)+wave(n-5,memo)
    return memo[n]
#bottom-up
def wave2(n):
    memo={0:0, 1:1, 2:1, 3:1, 4:2, 5:2}
    for idx in range(6, n+1):
        memo[idx] = memo[idx-1]+memo[idx-5]
    return memo[n]


for i in range(T):
    N = int(sys.stdin.readline().strip())
    # print(wave(N,memo_wave))
    print(wave2(N))
