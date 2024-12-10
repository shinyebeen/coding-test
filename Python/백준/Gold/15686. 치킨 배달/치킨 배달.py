n, m = map(int, input().split())
min_ans = 99999999

home = []
chicken = []

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(n):
        if row[j] == 1:
            home.append((i, j))
        elif row[j] == 2:
            chicken.append((i, j))

visited = [False] * len(chicken)

def dfs(idx, cnt):
    global min_ans

    if cnt == m:
        ans = 0
        for i in home:
            distance = 99999999
            for j in range(len(chicken)):
                if visited[j]:
                    check_num = abs(i[0]-chicken[j][0]) + abs(i[1]-chicken[j][1])
                    distance = min(distance, check_num)
            
            ans += distance
        min_ans = min(min_ans, ans)
        return 

    for i in range(idx, len(chicken)):
        if not visited[i]:
            visited[i] = True 
            dfs(i+1, cnt+1)
            visited[i] = False 

dfs(0, 0)
print(min_ans)