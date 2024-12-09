T = int(input())

for _ in range(T):
    n = int(input())
    arr = [[0, 0] for _ in range(n+2)]
    arr[0] = [1, 0]
    arr[1] = [0, 1]
    
    for i in range(2, n+1):
        arr[i] = [arr[i-1][0]+arr[i-2][0], arr[i-1][1]+arr[i-2][1]]

    print(*arr[n])
