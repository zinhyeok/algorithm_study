N = int(input())


#4
# 1, 3, 1 -> 4
ans = {1:1, 2:2, 3:3}
def sol(n):
    if n in ans:
        return ans[n]
    else:
        ans[n] = (sol(n-1)+sol(n-2))%10007
        return ans[n]

print(sol(N)%10007)

