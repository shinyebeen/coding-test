# 출발 : 상근이네
# 맥주 20개 든 박스 하나 들고 출발
# 50미터에 한 병씩 마심 -> 50미터를 가려면 그 직전에 맥주 한 병 마셔야 함
# 편의점에 들르면 빈병 버리고 새 맥주병을 살 수 있음
# But 박스에 들어있는 맥주는 20병을 넘을 수 없음
# 편의점을 나선 직후에도 50미터 가기 전에 맥주 한 병 마셔야 함
# 행복하게 페스티벌에 도착할 수 있는지 구하기

# 만약 두 좌표의 거리가 1000 이하인 경우 -> 이동 가능!
# 만약 두 좌표의 거리가 1000 초과인 경우 -> 이동 불가 ㅠ

import sys
input = sys.stdin.readline 

from collections import deque 

def bfs():
    q = deque()
    q.append([h_x, h_y])

    while q:
        x, y = q.popleft()

        if abs(x - f_x) + abs(y - f_y) <= 1000:
            print("happy")
            return 
        
        for i in range(n):
            if not visited[i]:
                new_x, new_y = c[i]
                if abs(x - new_x) + abs(y - new_y) <= 1000:
                    q.append([new_x, new_y])
                    visited[i] = 1

    print("sad")
    return

t = int(input())

for _ in range(t):
    n = int(input()) # 편의점 개수
    c = [] # 편의점 좌표 저장 리스트

    h_x, h_y = map(int, input().split()) # 상근이 집 좌표
    for i in range(n):
        c.append(list(map(int, input().split()))) # 편의점 좌표
    f_x, f_y = map(int, input().split()) # 페스티벌 좌표

    visited = [0 for _ in range(n)] # 편의점 방문 
    bfs()