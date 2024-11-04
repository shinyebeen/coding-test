def row(li):
    answer = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if li[i][j] == '.':
                cnt += 1
            else:
                if cnt >= 2:
                    answer += 1
                cnt = 0
        if cnt >= 2:
            answer += 1
    return answer

def col(li):
    answer = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if li[j][i] == '.':
                cnt += 1
            else:
                if cnt >= 2:
                    answer += 1
                cnt = 0
        if cnt >= 2:
            answer += 1

    return answer

n = int(input())
arr = [input() for _ in range(n)]
print(row(arr), end=' ')
print(col(arr))