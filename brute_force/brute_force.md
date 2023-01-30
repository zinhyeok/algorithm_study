# 브투트 포스(brute force)
brute force attack이 아닌 brute force search에 관한 내용

- brute: 무식한 force:힘 -> 무식한 방법으로 해석할 수 있다 
- 완전탐색 알고리즘으로 가능한 모든 경우의 수를 탐색하면서 결과를 가져오는 방법 
- 강력한 점은 예외 없이 100%의 확률로 정답을 출력한다 
- for/while loop을 이용한 탐색, 재귀함수를 이용한 방법, 크게 2가지로 문제를 해결하는 알고리즘이다

## 종류
- 선형구조: 순차탐색
- 비선형구조
  - 백트래킹, DFS, BFS

## 장단점
장점
- 알고리즘 설계와 구현이 매우 쉬운 편 
- 확실한 답을 찾을 수 있다 

단점
- 시간, 공간 복잡도 측면에서 모두 비효율적이다 -> 실제로 메모리 제한, 시간 제한에서 브루트포스로 풀 수 있는 문제인지 파악이 필요하다 
- 풀 수 없는 문제라면 다양한 기법을 추가함으로서 탐색범위나 시간을 줄일 수 있을 것이다(예: DP, binary search 등 적용)

## python으로 binary search 구현 
```python
import sys

N = int(input())
n_lst = list(map(int, sys.stdin.readline().split()))
M = int(input())
m_lst = list(map(int, sys.stdin.readline().split()))

n_lst.sort() #binary search need sorted array

def binary_search(data, target, start, end):
    print("{} {}".format(start, end))
    if start > end:
        return None
    mid = (start+end)//2

    if target == data[mid]:
        print("{}".format(data[mid]))
        return data[mid]
    elif data[mid] > target:
        #왼쪽 탐색
        return binary_search(data, target, start, mid-1)
    elif data[mid] < target:
        #오른쪽 탐색
        return binary_search(data,target,mid+1,end)
    else:
        return None

print(binary_search(n_lst, 10, 0, N - 1))
```
