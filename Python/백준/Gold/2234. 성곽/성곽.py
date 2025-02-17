from sys import stdin as s

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

m, n = map(int, s.readline().rstrip().split())
map_list = [list(map(int, s.readline().rstrip().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
area_list = list()

def dfs(x, y, num):
    q = [(x, y)]
    result = 1

    while q:
        x, y = q.pop()
        for k in range(4):
            if map_list[y][x] & (1 << k):
                continue
            
            ax, ay = x + dx[k], y + dy[k]

            if 0 <= ax < m and 0 <= ay < n and visited[ay][ax] == -1:
                visited[ay][ax] = num
                q.append((ax, ay))
                result += 1

    area_list.append(result)

cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == -1:
            visited[i][j] = cnt
            dfs(j, i, cnt)
            cnt += 1

print(cnt)
print(max(area_list))

result = 0 
for i in range(n):
    for j in range(m):
        for k in range(4):
            ai, aj = i + dy[k], j + dx[k]
            if 0 <= aj < m and 0 <= ai < n and visited[i][j] != visited[ai][aj]:
                result = max(result, area_list[visited[ai][aj]] + area_list[visited[i][j]])

print(result)