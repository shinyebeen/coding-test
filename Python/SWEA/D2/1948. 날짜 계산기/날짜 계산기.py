#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for test_case in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    if m1 == m2:
        answer = d2 - d1 + 1
    else:
        answer = month[m1]-d1 + d2 + 1
        for i in range(m1+1, m2):
            answer += month[i]
            
    print(f'#{test_case}', answer)