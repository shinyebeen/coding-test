from sys import stdin as s

n, d = map(int, s.readline().strip().split())
dp = [i for i in range(d+1)]

shortcuts = []

for _ in range(n):
    start, dest, length = map(int, s.readline().strip().split())
    if dest-start > length: # 만약 지름길 길이가 더 길면 해당 지름길은 사용 X
        shortcuts.append((start, dest, length))
    
shortcuts.sort() # start 기준 정렬

for start, dest, length in shortcuts:
    for i in range(1, d+1):
        if dest == i: # 지름길로 갈 수 있는 지점일 경우
            dp[i] = min(dp[i], dp[start]+length) # 해당 지점까지의 이동거리, 시작지점 이동거리 + 지름길 거리 중 작은 값 택
        else: # 지름길로 갈 수 없는 경우
            dp[i] = min(dp[i], dp[i-1]+1) # 해당 지점까지의 이동거리, 바로 직전 지점까지의 이동거리 + 1 중 작은 값 택

print(dp[d])