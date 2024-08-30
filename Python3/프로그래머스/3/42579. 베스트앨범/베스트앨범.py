def solution(genres, plays):
    d = {}
    
    idx = 0
    for g, p in zip(genres, plays):
        if g in d.keys():
            d[g].append((idx, p))
        else:
            d[g] = [(idx, p)]
        idx += 1
        
    l = list(d.values())
    l.sort(key = lambda x : (-sum(i[1] for i in x)))
    
    for i in range(len(l)):
        l[i] = sorted(l[i], key = lambda x : (- x[1], x[0]))
           
    answer = []
    
    for i in l:
        if len(i) == 1:
            answer.append(i[0][0])
            continue
            
        for j in range(2):
            answer.append(i[j][0])
    
    return answer