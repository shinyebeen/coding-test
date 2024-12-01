from collections import deque
from itertools import combinations

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

#벽
wall = []
#바이러스 후보 
virus_sub = []

for y in range(n) :
    for x in range(n) :
        if grid[y][x] == 1 :
            wall.append((y, x))
            
        elif grid[y][x] == 2 :
            virus_sub.append((y, x))
            grid[y][x] = 0 # 바이러스 후보 저장 후, 빈 공간으로 바꾸기

res = 10e9

for virus in combinations(virus_sub, m) :
    visited = [[0]*n for _ in range(n)]
    q = deque(virus)
    for y, x in virus :
        grid[y][x] = 2 
        visited[y][x] = 1

    #종료조건을 만들 cnt는 바이러스수 + 벽의 수 
    cnt = m + len(wall)

    while q:
        y, x = q.popleft()

        for d in range(4) :
            ny, nx = y + dy[d], x + dx[d]
            
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx] and grid[ny][nx] == 0 :
                visited[ny][nx] = visited[y][x] + 1 
                q.append((ny,nx))
                cnt += 1

            #맵이 다 바이러스가 되면 최솟값 갱신 
            if n**2 - cnt == 0:
                tmp = 0
                for i in range(n) :
                    tmp = max(max(visited[i]), tmp)
                
                if tmp < res :
                    res = tmp 
                break

    # 다음 조합 확인 전 다시 빈 공간으로 만들어주기 
    for y, x in virus :
        grid[y][x] = 0

if res >= 10e9 :
    print(-1)
else:
    print(res-1)