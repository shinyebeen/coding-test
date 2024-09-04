# 던전이 8개밖에 없으므로 순열로 모든 조합 만들어서 돌아도 됨

from itertools import permutations
def solution(k, dungeons):
    answer = 0
    dungeons = list(permutations(dungeons))
    
    for i in dungeons:
        curr_k = k
        cnt = 0
        for j in i:
            if curr_k >= j[0]:
                curr_k -= j[1]
                cnt += 1
                
        answer = max(answer, cnt)

    return answer