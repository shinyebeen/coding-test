n = int(input())
MOD = 1000000000

dp = [0] * (n + 1)
dp[0] = 1

powers = []
power = 1

# 2의 거듭제곱 리스트 생성
while power <= n:
    powers.append(power)
    power *= 2

for p in powers:
    for i in range(p, n + 1):
        dp[i] = (dp[i] + dp[i - p]) % MOD

print(dp[n])