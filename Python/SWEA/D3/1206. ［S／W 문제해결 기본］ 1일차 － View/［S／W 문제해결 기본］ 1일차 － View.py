for test_case in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    
    for i in range(2, len(arr)-2):
        m = min(arr[i]-arr[i-2], arr[i]-arr[i-1], arr[i]-arr[i+1], arr[i]-arr[i+2])
        if m > 0:
            cnt += m
    
    print(f'#{test_case} {cnt}')
