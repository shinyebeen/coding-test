def solution(places):
    answer = []
    
    def check(x1, y1, x2, y2):
        dist = abs(x1 - x2) + abs(y1 - y2)
        
        if dist == 1:
            return 0  # 바로 인접한 경우 거리두기 지킴X
        
        if dist == 2:
            if x1 == x2:  # 같은 행
                if place[x1][(y1 + y2) // 2] == 'O':
                    return 0
            elif y1 == y2:  # 같은 열
                if place[(x1 + x2) // 2][y1] == 'O':
                    return 0
            else:  # 대각선
                if place[x1][y2] == 'O' or place[x2][y1] == 'O':
                    return 0
                    
        return 1  # 거리두기 지킴
    
    for i in range(5):
        place = places[i]
        p = []  # P 좌표 저장

        for row in range(5):
            for col in range(5):
                if place[row][col] == 'P':
                    p.append([row, col])

        valid = 1
        for k in range(len(p)):
            x1, y1 = p[k]

            for l in range(k + 1, len(p)):  # k 이후만 탐색
                x2, y2 = p[l]
                
                if check(x1, y1, x2, y2) == 0:
                    valid = 0
                    break
            if valid == 0:
                break

        answer.append(valid)

    return answer
