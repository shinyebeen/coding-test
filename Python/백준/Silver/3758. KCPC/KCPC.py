from sys import stdin as s

T = int(s.readline().rstrip())

for _ in range(T):
    # 팀 개수, 문제 개수, 팀 ID, 로그 엔트리 개수
    n, k, t, m = map(int, s.readline().rstrip().split())
    
    # 팀 ID, 문제 번호, 획득 점수
    submit = [list(map(int, s.readline().strip().split())) for _ in range(m)]

    # 팀 ID, 점수, 제출 횟수, 마지막 제출 시간
    score = [[i, [0]*k, 0, 0] for i in range(n)]

    for i in range(m):
        if score[submit[i][0]-1][1][submit[i][1]-1] < submit[i][2]:
            score[submit[i][0]-1][1][submit[i][1]-1] = submit[i][2]
        score[submit[i][0]-1][2] += 1
        score[submit[i][0]-1][3] = i+1 

    for i in range(n):
        score[i][1] = sum(score[i][1])

    t_score = score[t-1]
    score.sort(key=lambda x : (-x[1], x[2], x[3]))
    
    print(score.index(t_score)+1)