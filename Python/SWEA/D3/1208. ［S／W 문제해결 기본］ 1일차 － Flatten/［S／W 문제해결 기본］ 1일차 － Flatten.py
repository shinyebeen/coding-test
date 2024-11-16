# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    n = int(input())
    h = list(map(int, input().split()))
    
    for i in range(n):
        if max(h) != min(h):
        	h[h.index(max(h))] -= 1
        	h[h.index(min(h))] += 1
        else:
            break
    print(f'#{test_case}', max(h)- min(h))
