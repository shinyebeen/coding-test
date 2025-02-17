from sys import stdin as s

n, k = map(int, s.readline().rstrip().split())
graph = [[*map(int, s.readline().rstrip().split())] for _ in range(n)]

for node in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][node] + graph[node][j])

def DFS(pos, cnt, cost):
    global res 

    if cnt == n:
        res = min(res, cost)
        return
    
    for next in range(n):
        if not visit[next]:
            visit[next] = 1
            DFS(next, cnt + 1, cost + graph[pos][next])
            visit[next] = 0 

visit = [0] * n
res = int(1e9)
visit[k] = 1 

DFS(k, 1, 0)
print(res)