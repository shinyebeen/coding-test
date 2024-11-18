n = int(input())
weights = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 0] for _ in range(n + 1)] # 노드 u를 포함했을 때와 하지 않았을 때의 최대 가중치 저장
visited = [0] * (n + 1)

def dfs(node):
    visited[node] = 1
    dp[node][1] = weights[node]  # 현재 노드를 포함하는 경우 : 초기값은 자신의 가중치
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)
            
            # 현재 노드를 포함하지 않는 경우 (자식 노드 포함O)
            dp[node][0] += max(dp[neighbor][0], dp[neighbor][1])
            
            # 현재 노드가 포함되어 있는 경우 : 서로 연결되어 있으면 안되므로 자식 노드는 반드시 포함되지 말아야 함
            dp[node][1] += dp[neighbor][0]

def find_members(node, include):
    visited[node] = 1
    if include:  # 현재 노드가 포함되어 있는 경우 : 서로 연결되어 있으면 안되므로 자식 노드는 반드시 포함되지 말아야 함
        members.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                find_members(neighbor, 0)
    else:  # 현재 노드를 포함하지 않는 경우
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dp[neighbor][0] >= dp[neighbor][1]:
                    find_members(neighbor, 0)
                else:
                    find_members(neighbor, 1)

dfs(1)

members = []
visited = [0] * (n + 1)
if dp[1][0] >= dp[1][1]:
    find_members(1, 0)
else:
    find_members(1, 1)

members.sort()
print(max(dp[1][0], dp[1][1]))
print(" ".join(map(str, members)))