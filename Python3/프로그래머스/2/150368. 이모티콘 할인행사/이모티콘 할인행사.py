def solution(users, emoticons):
    # users와 emoticons의 개수가 많지 않음. 브루트포스?
    
    ratios = []

    # ratios에 모든 할인율 조합 저장
    def all_price(depth, ratio):  # 재귀 깊이, 할인율 리스트
        nonlocal ratios
        
        if depth == len(emoticons):
            ratios.append(ratio[:])
            return
        
        for tmp in [0.1, 0.2, 0.3, 0.4]:
            ratio.append(tmp)
            all_price(depth + 1, ratio)
            ratio.pop()
            
    all_price(0, [])
    
    answer = []
    
    for ratio in ratios:
        subscriber, amount = 0, 0
        
        for user_ratio, user_price in users:
            tmp = 0
            
            for i in range(len(ratio)):
                if ratio[i]*100 >= user_ratio:
                    tmp += emoticons[i]*(1-ratio[i])

            if tmp >= user_price:
                subscriber += 1
            else:
                amount += tmp
                    
        answer.append([subscriber, int(amount)])   
    
    answer.sort(key=lambda x : (x[0], x[1]))
    
    return answer[-1]