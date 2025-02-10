from sys import stdin as s

r, c, n = map(int, s.readline().rstrip().split())
board = [list(s.readline().rstrip()) for _ in range(r)]

# 폭탄이 터질 방향
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 초기 상태 저장
if n == 1:
    for b in board:
        print("".join(b))
    exit()

# 짝수 초일 때: 모든 칸에 폭탄
if n % 2 == 0:
    for _ in range(r):
        print("O" * c)
    exit()

# 폭발을 시뮬레이션하는 함수
def explode(board):
    new_board = [["O"] * c for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            if board[i][j] == "O":
                new_board[i][j] = "."
                for dx, dy in d:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < r and 0 <= ny < c:
                        new_board[nx][ny] = "."
    
    return new_board

# 3초 후 상태
board1 = explode(board)
# 5초 후 상태 (3초 후 상태에서 다시 폭발)
board2 = explode(board1)

# n이 3 또는 7 또는 11 ... 일 때는 board1
# n이 5 또는 9 또는 13 ... 일 때는 board2
if n % 4 == 3:
    for b in board1:
        print("".join(b))
else:
    for b in board2:
        print("".join(b))
