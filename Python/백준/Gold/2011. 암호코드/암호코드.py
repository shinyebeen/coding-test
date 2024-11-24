code = [0] + list(map(int, list(input())))  # 2 5 1 1 4

dp = [1] + [0] * (len(code)-1) 

for i in range(1, len(code)):
    if code[1] == 0:
        break
    if code[i] > 0:
        dp[i] += dp[i-1]
    
    if 10 <= code[i-1]*10+code[i] <= 26:
        dp[i] += dp[i-2]

print(dp[-1]%1000000)