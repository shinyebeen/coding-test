from sys import stdin as s 

N = int(s.readline())
left_cnt = list(map(int, s.readline().strip().split())) # 왼쪽 사람 수
result = [0] * N

# 키가 작은 사람부터 시작하여, 각 사람이 적절한 자리에 배치될 수 있도록 한다.
for i in range(1, N+1):
    count = left_cnt[i-1]  # i번째 사람이 왼쪽에 있어야 하는 큰 사람 수
    
    for j in range(N):
        # 현재 자리가 비어있고, 남아있는 큰 사람의 수가 0일 때, 자리에 배치한다.
        if result[j] == 0 and count == 0:
            result[j] = i
            break
        elif result[j] == 0:
            # 현재 자리가 비어있다면, 큰 사람의 수를 감소시킨다.
            # 키가 작은 사람부터 줄서기 때문에 빈자리(나보다 큰 사람이 들어올 자리)라면 감소시켜야 함
            count -= 1

print(' '.join(map(str, result)))