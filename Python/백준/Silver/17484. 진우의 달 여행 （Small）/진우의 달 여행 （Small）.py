from sys import stdin as s

n, m = map(int, s.readline().strip().split())
matrix = [list(map(int, s.readline().strip().split())) for _ in range(n)]
dp = [[[0,0,0] for _ in range(m)]] + [[[float('inf'), float('inf'), float('inf')] for _ in range(m)] for _ in range(n)]

for i in range(1, n+1):
    for j in range(m):
        # 수직 방향, 대각선 오른쪽 방향
        if j < m-1:
            dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + matrix[i-1][j]

        # 수직 위, 왼쪽 위 값만 비교
        if 0 < j:
            dp[i][j][2] = min(dp[i-1][j-1][1], dp[i-1][j-1][0]) + matrix[i-1][j]

        # 1 : 수직 아래로 내려갈 예정
        # 왼쪽 위, 오른쪽 위 값 비교
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + matrix[i-1][j]
    
min_value = float('inf')
for row in dp[i]:
    for each in row:
        min_value = min(min_value, each)
print(min_value)