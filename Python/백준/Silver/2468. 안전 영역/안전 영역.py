# bfs로 탐색하면 될 것 같은데
# 영역 개수를 어떻게 세야할 지 모르겠음 ㅠ

# 가장 낮은 높이부터 최고 높이-1까지 모두 확인해야 함(최고 높이면 모두 물에 잠기기 때문에 최고 높이-1까지)

from collections import deque 

n = int(input())
graph = []
maxNum = 0

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        maxNum = max(graph[i][j], maxNum)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b, value, visited):
    q = deque([])
    q.append((a, b))
    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

result = 0
for i in range(maxNum):
    visited = [[0] * n for _ in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                cnt += 1
    
    result = max(cnt, result)

print(result)