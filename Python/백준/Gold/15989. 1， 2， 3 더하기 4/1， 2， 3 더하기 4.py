from sys import stdin as s

T = int(s.readline().strip())
dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i-2]

for i in range(3, 10001):
    dp[i] += dp[i-3]

for _ in range(T):
    n = int(s.readline().strip())
    print(dp[n])