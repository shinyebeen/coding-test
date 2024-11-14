T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    rot_90 = [i for i in zip(*arr[::-1])]
    rot_180 = [i for i in zip(*rot_90[::-1])]
    rot_270 = [i for i in zip(*rot_180[::-1])]

    print(f'#{test_case}')
    for i in range(n):
        print(''.join(map(str, rot_90[i])), end=' ')
        print(''.join(map(str, rot_180[i])), end=' ')
        print(''.join(map(str, rot_270[i])))