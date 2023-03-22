

#dp 아이디어 이용
# 1 -> 0 2->1 3->1 4->2 5->4->3->..
x = int(input())

def sol(x):
    dp = {1:0, 2:1, 3:1}
    for i in range(3,x+1):
        if i%3==0:
            dp[i] = min(dp[i//3], dp[i-1]) + 1
        elif i%2==0:
            dp[i] = min(dp[i // 2], dp[i - 1]) + 1
        else:
            dp[i] = dp[i-1] + 1
    print(dp[x])

sol(x)