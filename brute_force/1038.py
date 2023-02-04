from itertools import combinations

N = int(input())
ans = -1


# 감소하는 수
# 321
# 0 1 2 3 4 5 6 7 8 9 # 10 20 21 32 31 30... 98 97 ..91 90 #210 #3210 ... #9876543210

#감소하는 숫자 찾기 -> set((lst)) reverse sort이용
# 첫 시도 i를 무조건 0부터 시작 -> 문제 시간 초과
# 두번째 시도 각 숫자의 자리수에 따라서 숫자가 껑충 뛴다 이용 -> 시간초과
# 세번째 시도 조합으로 시도
num_list = []
for i in range(1,11):
    for num in combinations([0,1,2,3,4,5,6,7,8,9], i):
        num = list(num)
        num.sort(reverse=True) #(0,1) -> (1,0)
        num_list.append(int("".join(map(str, num)))) # 1,0 ->10

num_list.sort()

try:
    print(num_list[N])
except:
    print(-1)
