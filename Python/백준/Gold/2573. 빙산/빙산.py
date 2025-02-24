import sys
from collections import deque

input = sys.stdin.readline

# 방향 벡터 (상하좌우)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def melt_icebergs(icebergs):
    new_icebergs = []
    melted = [[0] * col for _ in range(row)]

    # 녹일 빙산만 확인
    for x, y in icebergs:
        sea_count = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and iceberg[nx][ny] == 0:
                sea_count += 1
        
        melted[x][y] = sea_count  # 각 빙산이 녹을 양 기록

    # 빙산 녹이기
    for x, y in icebergs:
        iceberg[x][y] = max(0, iceberg[x][y] - melted[x][y])
        if iceberg[x][y] > 0:
            new_icebergs.append((x, y))  # 녹은 후에도 남아 있으면 리스트에 추가
    
    return new_icebergs

def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and iceberg[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

def count_iceberg_groups(icebergs):
    visited = [[False] * col for _ in range(row)]
    count = 0
    
    for x, y in icebergs:
        if not visited[x][y]:
            count += 1
            bfs(x, y, visited)
    
    return count

# 입력 받기
row, col = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(row)]

# 초기 빙산 좌표 저장
icebergs = [(i, j) for i in range(row) for j in range(col) if iceberg[i][j] > 0]

year = 0
while icebergs:
    year += 1
    icebergs = melt_icebergs(icebergs)  # 빙산 녹이기
    
    if not icebergs:  # 빙산이 다 녹았으면
        print(0)
        exit()

    if count_iceberg_groups(icebergs) >= 2:  # 두 덩어리 이상이면
        print(year)
        exit()
