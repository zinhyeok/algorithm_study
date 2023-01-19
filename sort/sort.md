# Sorting(정렬)

- 정렬 알고리즘: n개의 숫자가 입력으로 주어졌을 때, 이를 사용자가 지정한 기준에 맞게 정렬하여 출력하는 알고리즘
- 다양한 알고리즘이 있지만, 대다수 O(n^2)이거나 O(nlogn)의 시간복잡도를 가진다.
- 본 정리는 기본적으로 오름차순정렬을 기준으로 작성되었다.

## 1. 선택정렬(Selection Sort)

- 선택정렬: 현재위치에 들어갈 값을 찾아서 정렬하는 배열. Min-selection sort, Max-selection sort로 나누어지고, 전자는 오름차순으로 후자는 내림차순으로 정렬한다
- 기본 로직: 가장 작은 원소를 앞으로 보내는 과정을 N-1번 반복한다

<img width="480" alt="img" src="https://gmlwjd9405.github.io/images/algorithm-selection-sort/selection-sort.png">

1️⃣ 주어진 배열 중 최솟값을 찾는다

2️⃣ 그 값을 맨 앞에 위치한 값과 교체한다

3️⃣ 다음 인덱스에서 이 과정을 N-1번 반복한다

``` python 
lst = [40,2,10,1,4,27,0,8]
  
for i in range(len(lst)-1):
    min_idx = i 
    for j in range(i+1, len(lst)):
      if lst[min_idx]>lst[j]:
          min_idx = j
    lst[i], lst[min_idx] = lst[min_idx], lst[i]

print(lst)
      
```
- 시간복잡도: O(n^2)
- n-1 + n-2 + n-3 + ... + 2 or 이중 for문 

## 2.삽입정렬(Insertion Sort)
- 이미 정렬된 배열 부분과 비교하여 자리를 정렬을 하는 알고리즘 
- sorted array와 unsorted array가 나누어져있을 때 유리 
<img width="700" src="https://gmlwjd9405.github.io/images/algorithm-insertion-sort/insertion-sort.png">

1️⃣ 두번째 원소부터 시작한다(혹은 unsorted data의 첫 원소) 

2️⃣ sorted 부분과 비교해 삽입할 위치를 찾는다(뒤에서 부터 훑는다)

3️⃣ 원소들을 뒤로 옮기고 지정된 위치에 자료를 삽입한다 이후 이를 N-1번 반복한다 

```python
lst = [40,2,10,1,4,27,0,8]
  
for i in range(1,len(lst)):
    for j in range(i, 0, -1):
        if lst[j-1]>lst[j]:
            lst[j-1], lst[j] = lst[j], lst[j-1]
        else:
          break
        
print(lst)
```
- 시간복잡도: O(n^2)
## 3.버블정렬(Bubble Sort)
- 버블 정렬: 서로 인접한 두 원소를 검사하여 정렬하는 알고리즘, 큰 것(혹은 작은 것)을 계속 위로 올리는 알고리즘
- 끝에서 부터 정렬이 완료된다 
<img width="700" src="https://gmlwjd9405.github.io/images/algorithm-insertion-sort/insertion-sort.png">

1️⃣ 첫번째 원소와 두번째 원소를 비교하여 교환한다. 두번째와 세번째를 비교하여 교환한다, 이 과정을 n번째와 비교할때까지 반복한다.

2️⃣ 두번째 원소도 같은 과정을 반복한다. 이때는 n-1번째까지와만 비교한다

3️⃣ 모든 원소를 정렬할 때 까지 해당과정을 반복한다

```python
lst = [40,2,10,1,4,27,0,8]

for i in range(len(lst)-1, 0, -1):
    for j in range(i):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
  
print(lst)
```
- 시간복잡도: O(n^2)
## 4. 병합정렬(Merge Sort)
 - 병합정렬: divide & conquer의 대표적인 예
 - O(nlogn)의 시간복잡도를 가짐
 <img width="664" alt="image" src="https://user-images.githubusercontent.com/91522259/210288396-3dab48ae-4add-42d6-b290-cc3cae4bfbb0.png">
 <img width="664" alt="image" src="https://gmlwjd9405.github.io/images/algorithm-merge-sort/merge-sort.png">
1️⃣ 입력배열을 같은 크기의 2개의 부분 배열로 분할한다

2️⃣ 부분 배열을 정렬한다. 이때 부분배열의 크기가 충분히 작지 않으면 재귀를 이용한다

3️⃣ 정렬된 부분배열을 병합한다(이 과정이 2번째 이미지에 있음)
```python 
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr
```
```python
def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))
```
- 메모리 효율이 좋지 않다
- 속도는 빠르다 
- 시간복잡도 증명은 t(n) = t(n/2) + t(n/2) + n임으로 t(1)=0에서 시작하여 t(n)일때까지 식을 전개하면 된다

## 5.퀵 정렬(Quick sort)
- pivot을 기준으로 pivot보다 작은 요소를 모두 왼쪽으로, pivot보다 큰 요소들은 오른쪽으로 옮긴다 
- 재귀를 이용한다 
- 보통은 random하게 pivot을 정하나, midian값을 이용하는 것이 더 안전하다 
<img width="537" alt="image" src="https://user-images.githubusercontent.com/91522259/210288024-b5255fe1-f6c8-4347-84bd-e9f8aa8fcde2.png">

1️⃣ 분할

- 피벗(교환하기 위한 기준) 설정 
- 왼쪽에서는 피벗보다 큰 데이터 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾는다, 아니면 넘어간다
- 큰 데이터와 작은 데이터의 위치를 서로 교환한다
- 두 값이 엇갈린 경우 종료하고, 피벗의 위치를 low(작은값)과 교환한다 

2️⃣ 왼쪽 리스트와 오른쪽 리스트를 똑같은 방식으로 정렬

```python
lst = [40,2,10,1,4]
def quick_sort(array, start, end):
	if start >= end: # 원소가 1개인 경우 종료
		return
	pivot = start # 피벗은 첫번째 원소
	left = start + 1
	right = end
	while left <= right:
		# 피벗보다 큰 데이터를 찾을 때까지 반복
		while left <= end and array[left] <= array[pivot]:
			left += 1
		# 피벗보다 작은 데이터를 찾을 때까지 반복
		while right >= start and array[right] >= array[pivot]:
			right -= 1
		if left > right : # 엇갈렸다면 작은 데이터와 피벗을 교체
			array[right], array[pivot] = array[pivot], array[right]
		else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
			array[left], array[right] = array[right], array[left]
	# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
	quick_sort(array, start, right-1)
	quick_sort(array, right+1, end)
  
quick_sort(lst, 0, len(array)-1)
print(lst)

```

- 시간복잡도는 평균의 경우 O(nlogn)이다
- n = 2^k라 하면 순환 호출은 k번이 필요할 것이다. 이때 각 경우에서 pivot을 이용해 정렬하는 연산은 N번 이루어진다. 
- 따라서 O(Kn) = O(nlogn)이다 

## 6. 계수 정렬(counting sort)
-시간복잡도 O(n)을 가지는 정렬 
- 데이터 값이 양수여야함 
- 값의 범위가 너무 크지 않아야한다 
- 메모리를 많이 사용한다
- 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적으로 사용 가능
<img width="537" src="https://velog.velcdn.com/images%2Fluvlik207%2Fpost%2F74c72cee-d764-4fcc-adff-e251677f54ae%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-09-24%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2010.58.00.png">

1️⃣ 계수 정렬(counting sort)을 위해 count 배열을 만들고, 배열(인덱스)를 앞에서부터 순회하면서 해당 원소가 몇번 나왔는지 기록한다

2️⃣ count배열을 이용해 누적합을 기록할 sum배열을 만든다(혹은 count배열을 누적합으로 변경한다)

누적합을 구하는 이유는 어느 인덱스에 원본 원소가 들어갈지 순서를 강제하기 위해서이다, 정렬된 원소들이 들어갈 배열의 인덱스를 카운팅배열의 데이터 - 1로 설정 해줌으로서 정해줄 수 있습니다, 필요한 이유는 1,2,2,3, 10001 의 case를 생각해보자

3️⃣ sum배열을 이용해 뒤에서부터 역순으로 원래 배열을 순회하며 기록한다

https://www.cs.miami.edu/home/burt/learning/Csc517.091/workbook/countingsort.html

```python
# 모든 원소의 값이 0보다 크거나 같다고 가정
# 정렬을 수행할 배열
arr = [4, 7, 9, 1, 3, 5, 2, 3, 4]

count = [0] * (max(arr) + 1)

for num in arr:
    count[num] += 1
    
for i in range(1, len(count)):
    count[i] += count[i-1]

result = [0] * (len(arr))

for num in arr:
    idx = count[num]
    result[idx - 1] = num
    count[num] -= 1

print(result)

# [1, 2, 3, 3, 4, 4, 5, 7, 9]
```
- 시간 복잡도 O(N+K), K는 데이터의 최대값의 크기 
- 공간복잡도: O(N+K)
- 동일한 값이 많을 때 사용하기 좋음, 값의 범위가 크면 사용하기 어려움 
## 7. radix sort
-bucket을 이용한 알고리즘 
-O(n)의 시간복잡도를 가지는 대표적인 알고리즘
-que 자료구조를 이용한다
<img width="480" src="https://mblogthumb-phinf.pstatic.net/20150809_22/kibum1223_1439077236991H7E1C_PNG/1.png?type=w2">
<img width="480" src="https://user-images.githubusercontent.com/86557453/213387769-c3b9ed38-f265-4a77-bad7-0fb8140243d4.png">
```python
def countingSort(arr, digit):
    n = len(arr)
  
    # 배열의 크기에 맞는 output 배열을 생성하고 10개의 0을 가진 count란 배열을 생성한다. 
    output = [0] * (n)
    count = [0] * (10)
    
    #digit, 자릿수에 맞는 count에 += 1을 한다. 
    for i in range(0, n):
        index = int(arr[i]/digit) 
        count[ (index)%10 ] += 1
 
    # count 배열을 수정해 digit으로 잡은 포지션을 설정한다.  
    for i in range(1,10):
        count[i] += count[i-1]  
        print(i, count[i])
    # 결과 배열, output을 설정한다. 설정된 count 배열에 맞는 부분에 arr원소를 담는다.   
    i = n - 1
    while i >= 0:
        index = int(arr[i]/digit)
        output[ count[ (index)%10 ] - 1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1

    #arr를 결과물에 다시 재할당한다.  
    for i in range(0,len(arr)): 
        arr[i] = output[i]
 
# Method to do Radix Sort
def radixSort(arr):
    # arr 배열중에서 maxValue를 잡아서 어느 digit, 자릿수까지 반복하면 될지를 정한다. 
    maxValue = max(arr)  
    #자릿수마다 countingSorting을 시작한다. 
    digit = 1
    while int(maxValue/digit) > 0: 
        countingSort(arr,digit)
        digit *= 10
 
arr = [ 170, 45, 75, 90, 802, 24, 2, 66]
#arr = [4, 2, 1, 5, 7, 2]
radixSort(arr)
 
for i in range(len(arr)):
    print(arr[i], end=" ")
```
- max element의 자릿수를 알아야한다, 혹은 max element를 알아야한다는 단점이 있다
✨ 코딩테스트에서 정렬 사용하기 
1. 내장되어 있는 정렬 기능 sorted(), .sort()를 이용한다
2. 정렬 알고리즘의 원리를 알고 있는지 확인하는 문제도 있다
3. 메모리 제한이 있는 경우도 있다. 해당 케이스를 주의하자 

🎓 참고 및 출처
https://hsp1116.tistory.com/33

https://gmlwjd9405.github.io/2018/05/06/algorithm-selection-sort.html

https://www.daleseo.com/sort-merge/

https://velog.io/@chappi/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-6%EC%9D%BC%EC%B0%A8-On-%EC%A0%95%EB%A0%AC-%EA%B3%84%EC%88%98-%EC%A0%95%EB%A0%AC

https://8iggy.tistory.com/123
