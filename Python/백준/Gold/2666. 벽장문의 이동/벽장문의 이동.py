import sys
input = sys.stdin.readline

n = int(input())
d1, d2 = map(int, input().split())
m = int(input())
orders = []

dp = [[[0 for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    orders.append(int(input()))

def solve(step, x, y):
    if step == m:
        return 0
    val = orders[step]
    dp[val][x][y] = min(abs(val-x)+solve(step+1, val, y), abs(val-y)+solve(step+1, x, val))

    return dp[val][x][y]

print(solve(0, d1, d2))