import sys

N = int(input())
count = [0]*10001
for i in range(N):
    x = int(sys.stdin.readline())
#개행문자 이슈로 인해 int()로 받아야함
    count[x] +=1


#for i in range(1, 10001):
#    count[i] += count[i-1]

for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)

'''
https://www.acmicpc.net/problem/10989 참고

1. 메모리 제한
sorted를 사용하려면 일단 배열을 만들어야함, 그러나 최대 개수가 10,000,000개임으로 배열을 저장하는 순간 메모리 초과가 됨
수는 10,000보자 작거나 같은 자연수이다 -> 수가 양수이고 숫자가 작다 -> counting sort를 이용 가능하다(redix sort도 불가능하다)
이때 누적합을 이용할 필요는 없다 -> 배열을 새로 만들 것이 아니기 때문
2. 시간제한
python은 input으로 입력을 받을 경우 느리다 -> sys.stdin.readline으로 해결하자
'''