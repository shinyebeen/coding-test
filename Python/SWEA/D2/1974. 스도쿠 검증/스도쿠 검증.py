# import sys
# sys.stdin = open("./ye-bin/input.txt", "r")

def check(sudoku):
    for i in range(9):
        check_r = set()
        check_c = set()
        for j in range(9):
            if 1<=sudoku[i][j]<=9 and sudoku[i][j] not in check_r:
                check_r.add(sudoku[i][j])
            else:
                return 0

            if 1<=sudoku[j][i]<=9 and sudoku[j][i] not in check_c:
                check_c.add(sudoku[j][i])
            else:
                return 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = set()
            for k in range(3):
                for l in range(3):
                    if 1<=sudoku[i+k][j+l]<=9 and sudoku[i+k][j+l] not in check:
                        check.add(sudoku[i+k][j+l])
                    else:
                        return 0  
    return 1    

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = 0
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{test_case}', check(sudoku))