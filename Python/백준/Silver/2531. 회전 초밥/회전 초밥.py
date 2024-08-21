from sys import stdin as s
from collections import deque

n, d, k, c = map(int, s.readline().strip().split())
sushi = [int(s.readline().strip()) for _ in range(n)]

start, end, res = 0, 0, 0
arr = deque()

while True:
    arr.append(sushi[end % n])

    if end - start == k-1:
        arr.append(c)
        res = max(res, len(set(arr)))
        
        arr.popleft()
        arr.pop()
        
        start += 1

        if start % n == 0:
            break

    end += 1

print(res)