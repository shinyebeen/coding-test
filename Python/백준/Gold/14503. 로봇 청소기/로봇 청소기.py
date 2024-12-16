n, m = map(int, input().split())
y, x, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

# 0:북, 1:동, 2:남, 3:서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

cnt = 0

while True:
    # 현재 칸 청소
    if room[y][x] == 0:
        cnt += 1
        room[y][x] = -1

    # 반시계 회전
    for _ in range(4):
        d = (d-1) % 4
        nx, ny = x + dx[d], y + dy[d]
        
        if 0 <= nx < m and 0 <= ny < n and room[ny][nx] == 0:
            x, y = nx, ny
            break  

    # 주변 4칸 중 청소되지 않은 빈칸이 없는 경우              
    else:
        x, y = x + dx[d]*(-1), y + dy[d]*(-1)
        if x >= m or x < 0 or y >= n or y < 0 or room[y][x] == 1:
            print(cnt)
            break