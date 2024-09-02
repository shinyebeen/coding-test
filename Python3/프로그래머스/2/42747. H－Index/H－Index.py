def solution(citations):
    citations.sort(reverse=True)
    
    for h in range(citations[0], -1, -1):
        over = 0
        under = 0
        for c in citations:
            if h <= c:
                over += 1
            else:
                under += 1
        
        if under <= h and over >= h:
            return h