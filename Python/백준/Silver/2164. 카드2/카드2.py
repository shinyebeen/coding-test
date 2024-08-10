from collections import deque
from sys import stdin as s

n = int(s.readline().strip())
card = deque(i for i in range(1, n+1))
turn = 0

while len(card) > 1:
    card.popleft()
    card.append(card[0])
    card.popleft()

print(card[0])
    

