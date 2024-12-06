import sys
input = sys.stdin.readline 

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        lego = [int(input()) for _ in range(n)]

        lego.sort()

        left, right = 0, n-1
        best = False

        while left < right:
            sum_ = lego[left] + lego[right]
            if sum_ == x:
                best = True
                print('yes', lego[left], lego[right])
                break 
            elif sum_ < x:
                left += 1
            else:
                right -= 1
        if not best:
            print('danger')
    except:
        break