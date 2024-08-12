from sys import stdin as s

t = int(s.readline().rstrip())

for _ in range(t):
    n = int(s.readline().rstrip())
    stock = list(map(int, s.readline().rstrip().split()))
    max_price = 0
    res = 0

    for i in range(n-1, -1, -1):
        if stock[i] > max_price:
            max_price = stock[i]
        else:
            res += max_price - stock[i]
    
    print(res)
            