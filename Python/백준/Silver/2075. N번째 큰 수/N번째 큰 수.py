import heapq
from sys import stdin as s

n = int(s.readline().strip())
heap = []

for _ in range(n):
    for item in map(int, s.readline().strip().split()):
        heapq.heappush(heap, item)

    if len(heap) > n:
        for _ in range(len(heap)-n):
            heapq.heappop(heap)

print(heap[0])