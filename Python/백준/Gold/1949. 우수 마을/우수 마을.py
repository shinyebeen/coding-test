import sys
sys.setrecursionlimit(10**6)

def dfs(node):
    visited[node] = True

    for i in graph[node]:
        if not visited[i]:
            dfs(i)
            dp[node][0] += max(dp[i][0], dp[i][1])
            dp[node][1] += dp[i][0]
    
n = int(input())
nums = [0] + list(map(int, input().split()))
graph = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
dp = [[0, nums[i]] for i in range(n+1)] #[i][0]: 우수마을 x, [i][1]: 우수마을

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(max(dp[1][0], dp[1][1]))