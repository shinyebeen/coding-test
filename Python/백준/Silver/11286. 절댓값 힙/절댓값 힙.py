import heapq
import sys 

n = int(input())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())

    if num != 0:
        heapq.heappush(heap, [abs(num), num])
    else:
        if len(heap)>0:
            print(heap[0][1])
            heapq.heappop(heap)
        else:
            print(0)