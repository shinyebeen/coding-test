#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    
    # 우, 하, 좌, 상
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    # 우측으로 이동 가능 -> 우방향 이동
    # 만약 우측으로 이동 불가능? -> 아래방향 이동
    # 만약 아래방향으로 이동 불가능? -> 좌방향 이동
    # 만약 왼쪽으로 이동 불가능? -> 위방향 이동
    # 만약 위로 이동 불가능? -> 우방향 이동 반복반복 하다가 만약 다 채워지면(가야할 칸이 0이 아니면) 종료
    
    x, y = 0, 0  # 현재 좌표
    d = 0  # 이동 방향

    for i in range(1, n**2+1):
        if arr[y][x] == 0:
            arr[y][x] = i
        
        nx, ny = x+dx[d], y+dy[d]

        if 0 > ny or ny >= n or 0 > nx or nx >= n or arr[ny][nx] > 0 :
            d = (d+1)%4
        y += dy[d]
        x += dx[d]
        
    print(f'#{test_case}')
    for i in range(n):
        print(*arr[i])
        