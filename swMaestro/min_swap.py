def min_swaps(s):
    s = s.split()
    lst = []
    for x in s:
        lst.append([i for i in x])
    count = 0
    s = lst
    #홀수번과 짝수번으로 처리
    for i in range(0, len(s)):
        if s[i][0] != s[i][1]:
            for j in range(i+1, len(s)):
                if s[j][1] == s[i][0]:
                    while True:
                        s[j-1][1], s[j][1] = s[j][1], s[j-1][1]
                        count += 1
                        print(s)
                        j = j-1
                        if s[i][0] == s[i][1]:
                            break
    return count


#ex1 input:AD BC CA DB
# AD BA CC DB
# AA BD CC DB
# AA BC DC DB
# AA BC CB DD
# AA BB CC DD
# output: 5

print(min_swaps(input()))
