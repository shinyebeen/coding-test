def solution(clothes):
    c = {}
    
    for i in clothes:
        if i[1] in c:
            c[i[1]] += 1
        else:
            # 안입는 경우도 있으므로 +1 해줌
            c[i[1]] = 2
    
    answer = 1
    
    for _, i in c.items():
        answer *= i
    
    return answer - 1