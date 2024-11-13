#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    string = input()
    for i in range(len(string)):
        if i>0 and string[:i] == string[i:i*2]:
            print(f'#{test_case}', i)
            break