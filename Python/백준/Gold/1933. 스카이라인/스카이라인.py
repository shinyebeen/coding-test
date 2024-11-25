import heapq

n = int(input())
arr = []
height = [0] * n
q = []

# 현재 index의 끝나는 점 저장
end = [0] * n

# 현재까지 끝난 끝점을 저장하는 set
check = set()

for i in range(n):
    l, h, r = map(int, input().split())
    # 시작점이면 1, 끝점이면 -1
    arr.append((l, i, 1))
    arr.append((r, i, -1))
    height[i] = h
    end[i] = r

# 1. 시점이 앞서는지
# 2. 시점이 같다면 시작점인지
# 3. 시점도 같고 둘 다 시작점이면 높이가 더 높은지
arr.sort(key=lambda x : (x[0], -x[2], -height[x[1]]))

now = 0 # 현재 최고높이
ans = []
for i in range(len(arr)):
    # point : 시점, idx : 건물의 인덱스, dir : 시작점인지 끝점인지
    point, idx, dir = arr[i]
    
    # 시작점인 경우
    if dir == 1:
        # 새 높이가 더 크면 => 그 부분이 새로운 스카이라인
        if now < height[idx]:
            now = height[idx]
            ans.append((point, now))
        # 높이와 상관없이 현재 건물의 높이와 끝점을 최대 힙에 저장
        heapq.heappush(q, (-height[idx], end[idx]))
        
    # 끝점인 경우
    else:
        # 현재 시점이 끝나면 set에 끝점의 시점 저장
        check.add(point)
        # 최대 높이가 끝난 건물이 아닐때까지 pop
        while q:
            if q[0][1] not in check:
                break
            heapq.heappop(q)
            
        # 힙이 비었다면 스카이라인의 높이는 0으로 갱신 => 건물이 끝났기 때문
        if not q:
            if now:
                now = 0
                ans.append((point, now))
                
        # 힙이 있다면 현재 높이와 비교 시 변동이 있다면 그 높이가 그 다음으로 높은 건물이기 때문에
        # 스카이라인 높이 갱신
        else:
            if -q[0][0] != now:
                now = -q[0][0]
                ans.append((point, now))

# 정답 출력
for i in ans:
    print(i[0], i[1], end=' ')