# dfs 백트래킹 문제...
# 모든 경기 조합을 미리 구해두고 dfs 돌리면서 1씩 빼고
# 전체 승무패의 합계가 0이 되는게 가능한지 구하기
from sys import stdin as s
from itertools import combinations 

def dfs(depth):
    global cnt 

    # 15번째 경기에 도달했을 때 
    if depth == 15:
        cnt = 1 
        for sub in res:
            if sub.count(0) != 3:
                cnt = 0
                break 
        return 

    g1, g2 = games[depth]
    
    for x, y in ((0,2), (1,1), (2,0)):
        if res[g1][x] > 0 and res[g2][y] > 0:
            res[g1][x] -= 1
            res[g2][y] -= 1
            dfs(depth+1)
            res[g1][x] += 1
            res[g2][y] += 1

answers = []
games = list(combinations(range(6), 2))

for _ in range(4):
    tmp = list(map(int, s.readline().strip().split()))
    res = [tmp[i:i+3] for i in range(0, 16, 3)]
    cnt = 0
    dfs(0)
    answers.append(cnt)

print(*answers)