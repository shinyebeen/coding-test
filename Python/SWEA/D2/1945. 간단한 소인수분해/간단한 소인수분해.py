# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
nums = [2, 3, 5, 7, 11]
for test_case in range(1, T+1):
    answer = [0, 0, 0, 0, 0]
    n = int(input())
    for i in range(5):
        while n % nums[i] == 0:
            n = n//nums[i]
            answer[i] += 1            
            
    print(f'#{test_case}', *answer)