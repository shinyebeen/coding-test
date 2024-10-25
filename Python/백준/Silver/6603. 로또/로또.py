from itertools import combinations

while True:
    s = list(map(int, input().split()))

    if s[0] == 0:
        break 
    
    lotto_nums = combinations(s[1:], 6)

    for i in lotto_nums:
        i = list(map(str, i))
        print(' '.join(i))
    
    print()