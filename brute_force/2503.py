import sys
from itertools import permutations

n = int(input())
numbers = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
#가능한 모든 경우의 수

for _ in range(n):
    #n회차 반복
    test, s, b = map(int, input().split())
    test = list(str(test))
    remove_cnt = 0 #제거한 수의 개수 index 확인용
#1회차
    for i in range(len(numbers)):
        s_cnt = b_cnt = 0
        i -= remove_cnt
        # 예를 들어 1 2 3 4 5 6 에서 3 제거 후 4를 확인해야하는 상황이면 1 2 4 5 6임으로 for 문에서는 i = 3이지만 실제 비교위치는 i = 2가 되어야함 그래서 필요
        num = numbers[i]
        for j in range(3):
            test[j] = int(test[j])
            if test[j] in num:
                if j == num.index(test[j]):
                    s_cnt += 1
                else:
                    b_cnt += 1

        if s_cnt != s or b_cnt != b:
            numbers.remove(num)
            remove_cnt += 1

print(len(numbers))