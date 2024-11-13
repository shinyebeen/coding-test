#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    answer = 0
    board = [list(map(int, input().split())) for _ in range(n)]
    
    for i in range(n):
        cnt_r = 0
        cnt_c = 0
        for j in range(n):
            if board[i][j] == 1:
                cnt_r += 1
            if board[i][j] == 0 or j == n-1:
                if cnt_r == k:
                    answer += 1
                cnt_r = 0
                
            if board[j][i] == 1:
                cnt_c += 1
            if board[j][i] == 0 or j == n-1:
                if cnt_c == k:
                    answer += 1
                cnt_c = 0

    print(f'#{test_case}', answer)