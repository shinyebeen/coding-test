# N, P, Q, X, Y 제공됨
# i가 0 이하인 경우 모두 1
# i가 1 이상인 경우
## A[int(i/P)-X] + A[int(i/Q)-Y]

n, p, q, x, y = map(int, input().split())
a = {}

def sol(i):
    global a
    
    if i <= 0:
        return 1
    
    if i in a:
        return a[i]

    a[i] = sol(i//p - x)+sol(i//q - y)
    return a[i]

print(sol(n))