def check(x, y, visited):
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        
        if (ax, ay) in visited:
            return False
        
    return True

def dfs(visited, total):
    global answer
    if total >= answer:
        return
    if len(visited) == 15:
        answer = min(answer, total)
    else:
        for i in range(1, n-1):
            for j in range(1, n-1):
                if check(i, j, visited) and (i, j) not in visited:
                    temp = [(i, j)]
                    temp_total = grid[i][j]
                    
                    for d in range(4):
                        ax = i + dx[d]
                        ay = j + dy[d]
                        temp_total += grid[ax][ay]
                        temp.append((ax, ay))
                    dfs(visited + temp, total + temp_total)
                    
n = int(input())
dx = [1, -1, 0 , 0]
dy = [0, 0, 1, -1]
result = []
grid = [list(map(int, input().split())) for _ in range(n)]
answer = int(1e9)

dfs([], 0)

print(answer)
