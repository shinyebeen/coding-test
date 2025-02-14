from sys import stdin as s

n = int(s.readline().rstrip())
board = []
teachers = []
res = False

for i in range(n):
    row = s.readline().rstrip().split()
    for j in range(n):
        if row[j] == 'T':
            teachers.append((i, j))
    board.append(row)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def check():
    for x, y in teachers:
        for i in range(4):
            nx, ny = x, y
            while 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 'O':  # 장애물 만나면 중단
                    break
                if board[nx][ny] == 'S':  # 학생 발견되면 실패
                    return False
                nx += dx[i]
                ny += dy[i]
    return True

def dfs(cnt):
    global res
    if res:
        return

    if cnt == 3:
        if check():
            res = True
        return

    for i in range(n):
        for j in range(n):
            if board[i][j] == 'X':
                board[i][j] = 'O'
                dfs(cnt + 1)
                board[i][j] = 'X'

dfs(0)
print("YES" if res else "NO")