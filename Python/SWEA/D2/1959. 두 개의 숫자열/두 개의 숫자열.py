#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    answer = 0
    
    max_len = a if n >= m else b
    min_len = b if n >= m else a
    
    for i in range(abs(n-m)+1):
        tmp = 0
        for j in range(len(min_len)):
            tmp += max_len[i+j]*min_len[j]
        answer = max(answer, tmp)
    
    print(f'#{test_case}', answer)
