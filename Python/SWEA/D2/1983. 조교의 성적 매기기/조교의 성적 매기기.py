T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    students = []
    
    for i in range(1, n+1):
        a, b, c = list(map(int, input().split()))
        a *= 0.35
        b *= 0.45
        c *= 0.2        
        students.append([a+b+c]+[i])
    
    students.sort(key=lambda x : -x[0])
    score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-']
    ratio = n//10
    
    for i in range(1, n+1): 
        if students[i][1] == k:
            print(f'#{test_case}', score[i//ratio])
            break