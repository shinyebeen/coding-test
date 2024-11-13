T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    set_num = set()
    i = 1
    while len(set_num) < 10:
        answer = n * i
        for num in str(answer):
            set_num.add(num)
        i+=1
    
    print(f'#{test_case}', answer)