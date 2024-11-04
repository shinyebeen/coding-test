from collections import deque 

def non(i, j, color):
    q = deque()
    q.append((i, j))
    graph_n[i][j] = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]

            if (0 <= nx < n) and (0 <= ny < n) and (graph_n[ny][nx]==0) and (grid[ny][nx]==color):
                q.append((ny, nx))
                graph_n[ny][nx] = 1
    
    return True 


def blind(i, j, color):
    q = deque()
    q.append((i, j))
    graph_b[i][j] = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]

            if (0 <= nx < n) and (0 <= ny < n) and (graph_b[ny][nx]==0):
                if (color=='R' or color=='G') and (grid[ny][nx]=='R' or grid[ny][nx]=='G'):
                    q.append((ny, nx))
                    graph_b[ny][nx] = 1
                elif grid[ny][nx] == color:
                    q.append((ny, nx))
                    graph_b[ny][nx] = 1
    return True 


n = int(input())
grid = []
for _ in range(n):
    grid.append(input())
    
graph_n = [[0]*n for _ in range(n)]
graph_b = [[0]*n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = [0, 0]

for i in range(n):
    for j in range(n):
        if graph_n[i][j] == 0:
            if non(i, j, grid[i][j]):
                result[0] += 1
        if graph_b[i][j] == 0:    
            if blind(i, j, grid[i][j]):
                result[1] += 1
print(*result)