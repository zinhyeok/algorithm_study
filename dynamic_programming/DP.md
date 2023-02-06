# 다이나믹 프로그래밍 Dynamic Programming 
동적 계획법, 동적 프로그래밍이라고 한다. 기억하기 프로그래밍이라는 용어를 쓰는 교수님도 있다고 한다

복잡한 문제를 간단한 여러개의 문제로 나누어 푸는 방법이다(분할정복(Divide & Conquer)과 동적 프로그래밍은 주어진 문제를 작게 쪼개서 하위 문제로 해결하고 연계적으로 큰 문제를 해결한다는 점은 같다.

차이점은, 분할 정복은 분할된 하위 문제가 동일하게 중복이 일어나지 않는 경우에 쓰며, 동일한 중복이 일어나면 동적 프로그래밍을 쓴다) 


이 때 재귀함수를 호출할때 반복적으로 계산되는 것들의 계산 횟수를 줄이고자 이전에 값을 계산하지 않고 가져오는 메모이제이션이 동적 프로그래밍 중 하나이다. 

대표적으로 피보나치 수열 구현이 있다. 

## 다이나믹 프로그래밍은 언제 사용하는가? 
DP가 적용되기 위해서는 아래의 2조건을 만족해야한다. 
1) Overlapping Subproblems(겹치는 부분 문제) -> 피보나치와 점화식
2) Optimal Substructure(최적 부분 구조) -> 부분의 최적 결과가 전체 문제에도 동일하게 적용시

## 구현 방법 
- Bottom-up: 반복문을 사용해, 아래에서부터 계산을 수행하고 전체 문제를 해결하는 방식
 
 Tabulation이라고 부른다(table-filling, 즉, 기저상태(0)부터 위로 쌓아올라간다라는 의미)

- Top-Down: 재귀를 사용하여, 위에서부터 값을 호출해 아래로 내려간 다음, 해당 결과 값을 재귀를 통해 다시 부르는 방식

## 피보나치 수열 구현 
<img width = "200" src="https://s3-ap-northeast-2.amazonaws.com/opentutorials-user-file/module/5371/12562.jpg">

### 방법 1 단순 재귀 

```ptyhon 
n = int(input()) # 몇번째 피보나치?

# 단순 재귀함수. 밑의 두 방법에 비해 비효율적
def fibo(n):
    if n <= 1:
        return n
    return fibo1(n-1) + fibo1(n-2)
```
<img width="500" src="https://shoark7.github.io/assets/img/algorithm/fibbonacci-recurisive.png">

단순 재귀로 구현시 n이 6 이상만 되도 시간이 오래 걸릴 것이다. 그 이유는 그림과 같이 n이 커길 수록 트리의 크기가 기하급수적으로 커지기 때문이다. 
따라서 이미 구한 값을 저장해두고 재사용하는 방법을 택한다(memoization)

```python
n = int(input()) # 몇번째 피보나치?
table = [0] * (n + 1) # for memoization


# Top-down 방식을 이용한 DP 재귀 
def fibonacci_top(n):
  if n<2:
    return table(n) = n
  if table[n] > 0:
    return table[n]
  table[n] = fibonacci_top(n-1) + fibonacci_top(n-2)
  return table[n]
  
# dict이용 
fib_memo = {}
def fibonacci(n):
    if n in fib_memo:
        return fib_memo[n]
    else:
        fib_memo[n] = n if n < 2 else fibonacci(n-2) + fibonacci(n-1)
        return fib_memo[n]
        
# Bottom-up 방식을 이용한 DP 반복문, n까지 모두 for문을 통해 구한다  
def fibonacci_lst(n):
    x = [i for i in range(n+1)]
    for idx in range(2, n+1):
        x[idx] = x[idx-2] + x[idx-1]
    return x[n]

```

🎓 참고 자료

https://hongjw1938.tistory.com/47
