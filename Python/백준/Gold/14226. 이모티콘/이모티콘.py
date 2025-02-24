from collections import deque 

s = int(input())
visited = [[0 for _ in range(s*3+1)] for _ in range(s*3+1)]  # 배열 크기 넉넉하게 설정
q = deque()
q.append([0, 1, 0])  # time, display, clipboard

while q:
    time, display, clipboard = q.popleft()
    if display == s:
        print(time)
        break 

    if not visited[display][clipboard]:
        visited[display][clipboard] = 1

        if display >= 1:
            q.append([time+1, display-1, clipboard])  
            q.append([time+1, display, display])  

        if clipboard and display + clipboard < len(visited):  # 범위 체크
            q.append([time+1, display+clipboard, clipboard])
