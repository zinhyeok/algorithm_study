def check(str):
    lst = []
    for i in range(len(str)):
        if str[i] == '(':
            lst.append('(')
        else:
            if len(lst) > 0:
                lst.pop()
            else:
                return "NO"
    if len(lst) == 0:
        return "YES"
    else:
        return "NO"

N = int(input())
for _ in range(N):
    print(check(input()))

