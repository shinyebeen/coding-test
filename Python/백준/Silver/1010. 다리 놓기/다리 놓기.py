from math import factorial
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    if n == 1:
        print(m)
    else:
        print(factorial(m)//(factorial(m-n)*factorial(n)))