from collections import deque
def bfs(n, nodes, node1, node2):
    visited = [0 for _ in range(n+1)]
    q = deque([node1])
    cnt = 0
    
    while q:
        x = q.popleft()
        visited[x] = 1
        
        if x == node2:
            continue
        
        for i in range(len(nodes[x])):
            if visited[nodes[x][i]] == 0:
                q.append(nodes[x][i])
                cnt += 1
    
    return cnt
        

def solution(n, wires):
    nodes = [[] for _ in range(n+1)]
    for i in range(len(wires)):
        nodes[wires[i][0]].append(wires[i][1])
        nodes[wires[i][1]].append(wires[i][0])
    
    answer = 101

    for n1, n2 in wires:
        answer = min(answer, abs(bfs(n, nodes, n1, n2)-bfs(n, nodes, n2, n1)))
    
    return answer