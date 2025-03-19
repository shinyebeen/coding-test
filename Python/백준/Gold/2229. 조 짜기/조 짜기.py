n = int(input())
students = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    minval = maxval = students[i]
    for j in range(i+1, n):
        minval = min(minval, students[j])
        maxval = max(maxval, students[j])
        dpval = dp[i-1] if i > 0 else 0
        dp[j] = max(dp[j], maxval-minval+dpval)
        
print(dp[-1])