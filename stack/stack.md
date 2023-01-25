# Stack(스택)

- 한 쪽 끝에서만 자료를 넣고 뺄 수 있는 **LIFO(Last in First out)** 자료구조 
- 가장 최근에 저장된 데이터가 가장 먼저 나온다 
- 예시: 인터넷 브라우저의 뒤로 가기 / 각 종 되돌리기 가기/ 설거지거리 / 프링글스 / 시스템 스택

<img width="500" src="https://blog.kakaocdn.net/dn/CSWsW/btq2t9Wc0um/qTQgiVXqjxA0l9weuUKTH1/img.png">


## 용어 
삽입(insert)와 삭제(delete)를 리스트의 한쪽(top)에서 실행함 

-상단(stack top, top) : 스택에서 입출력이 이루어지는 부분
- 요소(element): 스택에 저장되는 것
- 공백 스택(empty stack): 요소가 없는 스택
- full 스택(full stack): 포화 상태의 스택

## 연산 
- top(): 스택 맨 위의 데이터를 반환 
- push(): 스택 맨 위에 데이터 삽입
- pop(): top과 동일하나 데이터를 삭제하면서 반환(pop하고 튀어나옴)
- isEmpty(): boolean type 반환, 스택에 원소가 비어있으면 true, 아니면 false
- isfull(): boolean type 반환, 스택에 원소가 모두 차있으면 true, 아니면 false

## python에서 구현 
- 스택도 선형자료구조이기에 배열이나 list를 이용해 구현 가능 
- python에서는 따로 stack을 내부적으로 구현해있지는 않음
- list에 pop(), append()가 존재한다, 둘 다 last(top) 요소를 제거하거나 추가하는 연산이기에 이로 대체해서 사용 가능 
- isEmpty(), isfull()은 따로 구현해야함, 다만 list는 크기가 고정된 자료구조가 아님

```python
stack = [1,2,3,4,5]
stack.pop()
>> 5, stack = [1,2,3,4]
stack.append(8)
>> stack = [1,2,3,4,8]
```
