lst = input().split('-')

#무조건 -는 마지막에 처리한다
#0으로 시작하는 숫자처리하기
num_lst = []
for i in lst:
    num_lst.append(sum(list(map(int, i.split('+')))))


ans = num_lst[0] - sum(num_lst[1:])


print(ans)







