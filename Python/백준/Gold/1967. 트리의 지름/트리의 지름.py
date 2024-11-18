n = int(input().strip())
graph = [[] for _ in range(n+1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    
    graph[u].append((v, w))
    graph[v].append((u, w))

def dfs(start):
    # 각 노드의 방문 여부와 거리 기록
    visited = [-1] * (n + 1)
    stack = [(start, 0)]  
    visited[start] = 0         
    node, max_dist = start, 0

    while stack:
        current, current_dist = stack.pop()
        
        if current_dist > max_dist:
            node = current
            max_dist = current_dist
        
        # 인접 노드 방문
        for neighbor, dist in graph[current]:
            if visited[neighbor] == -1:
                visited[neighbor] = current_dist + dist
                stack.append((neighbor, current_dist + dist))

    # 가장 먼 노드와 그 노드까지의 거리 반환
    return node, max_dist

# 루트 노드에서 가장 먼 노드 찾기
node, _ = dfs(1)

# 해당 트리에서 제일 멀리 떨어져있는 노드 간 거리 찾기
_, max_dist = dfs(node)

print(max_dist)