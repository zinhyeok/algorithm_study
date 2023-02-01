lst_dwarf = []
ans = []
#키 넣기
for i in range(9):
    lst_dwarf.append(int(input()))

# 조합 만들기 함수
def combination(lst, r):
    wanted = []
    if r == 1:
        for i in lst:
            wanted.append([i])
    else:
        for i in range(len(lst)-r+1):
            for j in combination(lst[i+1:], r-1):
                wanted.append([lst[i]]+j)
    return wanted

#조합 만들기
combination_dwarf = combination(lst_dwarf, 7)
for i in combination_dwarf:
    if sum(i) == 100:
        ans = i
        ans.sort()
        break

for i in ans:
    print(i)

