def row(li):
    answer = [0, 0]
    for i in range(n):
        cnt_r, cnt_c = 0, 0
        for j in range(n):
            # 가로
            if li[i][j] == '.':
                cnt_r += 1
            else:
                if cnt_r >= 2:
                    answer[0] += 1
                cnt_r = 0
            # 세로
            if li[j][i] == '.':
                cnt_c += 1
            else:
                if cnt_c >= 2:
                    answer[1] += 1
                cnt_c = 0
                
        if cnt_r >= 2:
            answer[0] += 1
        if cnt_c >= 2:
            answer[1] += 1

    return answer

n = int(input())
arr = [input() for _ in range(n)]

print(*row(arr))