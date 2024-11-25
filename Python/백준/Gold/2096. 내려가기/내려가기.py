n = int(input())
arr = list(map(int, input().split()))
max_dp = arr 
min_dp = arr 

for _ in range(n-1):
    arr = list(map(int, input().split()))
    max_dp = [arr[0]+max(max_dp[0], max_dp[1]), arr[1]+max(max_dp[0], max_dp[1], max_dp[2]), arr[2]+max(max_dp[2], max_dp[1])]
    min_dp = [arr[0]+min(min_dp[0], min_dp[1]), arr[1]+min(min_dp[0], min_dp[1], min_dp[2]), arr[2]+min(min_dp[2], min_dp[1])]

print(max(max_dp), min(min_dp))