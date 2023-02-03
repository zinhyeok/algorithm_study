first_num = int(input())
len_result = 0
result = []

for i in range(first_num+1):
    lst = [first_num, i]
    j = 0
    while True:
        last_num = lst[j] - lst[j+1]
        j += 1
        if last_num < 0:
            break
        lst.append(last_num)
        if len_result < len(lst):
            len_result = len(lst)
            result = lst[:]

print(len_result)
for i in result:
    print(i, end=" ")