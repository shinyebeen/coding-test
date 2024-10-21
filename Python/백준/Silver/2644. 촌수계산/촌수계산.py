# 입력값 받는 부분
N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = -1  # 최단 경로를 저장할 변수, 기본값 -1로 설정 (경로가 없을 경우)

# 어떤 노드들이 연결되어 있는지 graph라는 2차원 배열에 저장
for _ in range(M):
    x, y = map(int, input().split())  
    graph[x].append(y)
    graph[y].append(x)

# dfs
def dfs(v, num):
    global result
    visited[v] = True

    if v == B:
        result = num  # B에 도착하면 현재 경로 길이(촌수)를 저장
        return True   # 경로를 찾으면 True 반환하여 재귀 종료

    for i in graph[v]:
        if not visited[i]:
            if dfs(i, num + 1):  # 경로를 찾으면 바로 종료
                return True

    return False  # 경로를 찾지 못했으면 False 반환

# dfs 실행
dfs(A, 0)
print(result)