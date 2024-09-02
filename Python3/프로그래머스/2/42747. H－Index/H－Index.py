def solution(citations):
    citations.sort(reverse=True)
  
    for i in range(len(citations)):
        if citations[i] <= i:
            return i
    return len(citations)

#     for h in range(citations[0], -1, -1):
#         cnt = 0
#         for c in citations:
#             if h <= c:
#                 cnt += 1
        
#         if cnt >= h:
#             return h