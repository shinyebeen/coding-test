#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    m = [0]*8
    n = int(input())
    for i in range(8):
        if n//money[i] > 0:
            m[i] = n//money[i]
            n = n%money[i]
            
    print(f'#{test_case}')
    print(*m)
    
