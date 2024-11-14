#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    pascal = [[0], [1], [1, 1]]

    for i in range(3, n+1):
        nums = [1]
        for j in range(1, i-1):
            nums.append(pascal[i-1][j-1]+pascal[i-1][j])
        nums.append(1)
        
        pascal.append(nums)
    
    print(f'#{test_case}')
    for i in range(1, n+1):
        print(*pascal[i])