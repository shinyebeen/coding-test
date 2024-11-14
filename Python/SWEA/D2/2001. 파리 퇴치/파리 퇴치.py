T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split()) 
    flys = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    
    for i in range(n-m+1): # 행반복
    	for j in range(n-m+1): # 열반복
            cnt = 0
            for k in range(m):
                cnt += sum(flys[j+k][i:i+m])
            answer = max(answer, cnt)

    print(f'#{test_case} {answer}')
