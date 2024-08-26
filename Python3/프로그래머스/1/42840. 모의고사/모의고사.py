import math

def solution(answers):
    res = []
    
    person_1 = [1, 2, 3, 4, 5] * math.ceil(len(answers)/5)
    person_2 = [2, 1, 2, 3, 2, 4, 2, 5] * math.ceil(len(answers)/8)
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * math.ceil(len(answers)/10)

    cnt = [0, 0, 0]
    max_cnt = 0

    for i in range(len(answers)):
        if answers[i] == person_1[i]:
            cnt[0] += 1
        if answers[i] == person_2[i]:
            cnt[1] += 1
        if answers[i] == person_3[i]:
            cnt[2] += 1
        
    for i in range(3):
        if cnt[i] > max_cnt:
            res = [i+1]
            max_cnt = cnt[i]
        elif cnt[i] == max_cnt:
            res.append(i+1)
    
    res.sort() 
    return res