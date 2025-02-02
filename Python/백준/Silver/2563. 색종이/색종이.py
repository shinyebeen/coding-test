n = int(input())
board = [[0]*100 for _ in range(100)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y-1, 10+y-1):
        for j in range(x-1, 10+x-1):
            board[i][j] = 1

print(sum(map(sum, board)))