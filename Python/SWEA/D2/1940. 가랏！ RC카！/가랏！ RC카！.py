#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    command = [list(map(int, input().split())) for _ in range(n)]
    current = 0  # 현재속도
    answer = 0  # 이동거리
    
    for i in range(len(command)):
        if command[i][0] == 0: # 속도 유지
            answer += current
        elif command[i][0] == 1: # 가속
            current += command[i][1]
            answer += current
        else:
            current = current - command[i][1] if current >= command[i][1] else 0
            answer += current
    
    print(f'#{test_case} {answer}')