import sys 
input = sys.stdin.readline

# i에서 k로 바로 이동할 수 있는 간선 존재해야 함
# 그 간선을 edge[i][k]라고 하고 최단경로 길이를 dist[i][j]라고 둠
# 그 간선이 최단경로 상에 존재해야 하므로, 부분 최단 경로를 만족시킴
## dist[i][j] = edge[i][k] + dist[k][j] 만족
# 모든 i, j, k에 대해 이를 검사해야 하고 n이 최대 200이므로 플로이드 워셜 알고리즘 사용 가능(O(N^3))

MAX = float('inf')

n, m = map(int, input().split())
edge_mat = [[MAX]*n for _ in range(n)]
dist_mat = [[MAX]*n for _ in range(n)]
ans = [[0]*n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edge_mat[a-1][b-1] = edge_mat[b-1][a-1] = c
    dist_mat[a-1][b-1] = dist_mat[b-1][a-1] = c 

for k in range(n):
    dist_mat[k][k] = 0

    for i in range(n-1):
        for j in range(i+1, n):
            if j == k or i == k:
                continue
            if dist_mat[i][j] > dist_mat[i][k] + dist_mat[k][j]:
                dist_mat[i][j] = dist_mat[j][i] = dist_mat[i][k] + dist_mat[k][j]

for i in range(n):
    for j in range(n):
        if i == j:
            ans[i][j] = '-'
            continue
        for k in range(n):
            if i == k or edge_mat[i][k] == MAX:
                continue
            if edge_mat[i][k] + dist_mat[k][j] == dist_mat[i][j]:
                ans[i][j] = k+1
                break

for _ans in ans:
    print(*_ans)
