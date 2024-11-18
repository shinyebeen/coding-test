import sys
from collections import deque

n = int(input())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
shark_x, shark_y, shark_size = 0, 0, 2

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            shark_x, shark_y = i, j
            arr[i][j] = 0  # 상어 위치를 0으로 초기화

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, size):
    visited = [[0] * n for _ in range(n)]
    queue = deque([(x, y, 0)])  # x좌표, y좌표, 거리
    visited[x][y] = 1
    fishes = []

    while queue:
        x, y, dist = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:

                if arr[nx][ny] <= size:
                    visited[nx][ny] = 1

                    if 0 < arr[nx][ny] < size:  # 먹을 수 있는 물고기
                        fishes.append((dist + 1, nx, ny))
                    else:  # 이동만 가능한 칸
                        queue.append((nx, ny, dist + 1))

    # 먹을 수 있는 물고기 중 거리, 위쪽, 왼쪽 순으로 정렬
    fishes.sort(key=lambda fish: (fish[0], fish[1], fish[2]))
    return fishes[0] if fishes else None

# 시뮬레이션 실행
time = 0
cnt = 0

while True:
    target = bfs(shark_x, shark_y, shark_size)
    if target is None:
        break

    dist, nx, ny = target
    time += dist  # 이동 시간 추가
    shark_x, shark_y = nx, ny  # 상어 위치 갱신
    arr[nx][ny] = 0  # 물고기를 먹은 자리 비우기
    cnt += 1

    if cnt == shark_size:  # 상어 크기 증가 조건
        shark_size += 1
        cnt = 0

print(time)
