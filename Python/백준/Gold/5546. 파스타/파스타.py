import sys
input = sys.stdin.read

def solve():
    MOD = 10000
    
    # 입력 처리
    data = input().split()
    N = int(data[0])  # 총 날짜 수
    K = int(data[1])  # 강제 지정된 날의 수
    fixed = {}  # 특정 날에 지정된 파스타 정보
    
    index = 2
    for _ in range(K):
        day = int(data[index])
        pasta = int(data[index + 1])
        fixed[day] = pasta
        index += 2
    
    # DP 테이블 초기화
    dp = [[[0] * 3 for _ in range(3)] for _ in range(N + 1)]
    
    # 첫날 초기화
    if 1 in fixed:
        p = fixed[1] - 1
        dp[1][p][0] = 1  # count=0 의미: 첫날이므로 연속된 횟수 없음
    else:
        for p in range(3):
            dp[1][p][0] = 1
    
    # DP 계산
    for day in range(2, N + 1):
        if day in fixed:
            p = fixed[day] - 1
            for prev_p in range(3):
                for cnt in range(2):
                    if prev_p == p:
                        dp[day][p][cnt + 1] = (dp[day][p][cnt + 1] + dp[day - 1][p][cnt]) % MOD
                    else:
                        dp[day][p][0] = (dp[day][p][0] + dp[day - 1][prev_p][cnt]) % MOD
        else:
            for p in range(3):
                for prev_p in range(3):
                    for cnt in range(2):
                        if prev_p == p:
                            dp[day][p][cnt + 1] = (dp[day][p][cnt + 1] + dp[day - 1][p][cnt]) % MOD
                        else:
                            dp[day][p][0] = (dp[day][p][0] + dp[day - 1][prev_p][cnt]) % MOD
    
    # 결과 계산
    result = sum(dp[N][p][cnt] for p in range(3) for cnt in range(2)) % MOD
    print(result)

if __name__ == "__main__":
    solve()