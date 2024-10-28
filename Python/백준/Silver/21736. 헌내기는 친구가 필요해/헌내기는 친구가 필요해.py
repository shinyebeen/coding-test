from collections import deque

n, m = map(int, input().split())
campus = []

for i in range(n):
    campus.append(input())

    if 'I' in campus[i]:
        doyeon = [campus[i].index('I'), i]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(d_x, d_y):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque([[d_x, d_y]])
    cnt = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == 0:
                visited[ny][nx] = 1

                if campus[ny][nx] == 'P':
                    cnt += 1
                    q.append([nx, ny])

                elif campus[ny][nx] == 'O':
                    q.append([nx, ny])

    return cnt 

cnt = bfs(doyeon[0], doyeon[1])

if cnt == 0:
    print('TT')
else:
    print(cnt)