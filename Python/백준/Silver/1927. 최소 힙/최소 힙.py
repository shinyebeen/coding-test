from sys import stdin as s
import heapq

n = int(s.readline().strip())
heap = []

for _ in range(n):
    x = int(s.readline().strip())

    if x == 0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)