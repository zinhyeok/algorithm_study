from collections import deque

cards = deque()

N = int(input())
for i in range(N):
    cards.append(i+1)

for i in range(N-1):
    cards.popleft()
    last_card = cards.popleft()
    cards.append(last_card)

print(cards.pop())