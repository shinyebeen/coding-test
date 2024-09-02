# I 숫자 : INSERT
# D 1 : 최댓값 삭제
# D -1 : 최솟값 삭제

from heapq import heappop, heappush

def solution(operations):
    operations = [i.split() for i in operations]
    queue = []
    
    for o, n in operations:
        n = int(n)
        
        if o == 'I':
            heappush(queue, n)
        elif queue:
            if n == 1:
                queue.sort()
                queue.pop()
                
            elif n == -1:
                heappop(queue)
                
    if len(queue) == 0:
        return [0, 0]
    
    queue.sort()
    return [queue[-1], queue[0]]