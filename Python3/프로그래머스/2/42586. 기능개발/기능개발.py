# day.append(math.ceil((100 - progress[i]) / speeds[i]))
# day[0]부터 시작
# day[0]보다 작거나 같으면 cnt += 1
# day[0]보다 큰 값 나타나면 answer.append(cnt); cnt=0

import math
def solution(progresses, speeds):
    answer = []
    day = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
    d = day[0]
    cnt = 1
    
    for i in range(1, len(progresses)):
        if day[i] <= d:
            cnt += 1
        else:
            answer.append(cnt)
            d = day[i]
            cnt = 1
            
    answer.append(cnt)
        
    return answer