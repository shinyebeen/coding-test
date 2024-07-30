import sys
input = sys.stdin.readline

S = set()
M = int(input().strip())

all_elements = set(str(i) for i in range(1, 21))
result = []

for _ in range(M):
    order = input().strip().split()
    
    if order[0] == 'add':
        S.add(order[1])
    elif order[0] == 'remove':
        S.discard(order[1])
    elif order[0] == 'check':
        print(1) if order[1] in S else print(0)
    elif order[0] == 'toggle':
        if order[1] in S:
            S.remove(order[1])
        else:
            S.add(order[1])
    elif order[0] == 'all':
        S = all_elements.copy()
    elif order[0] == 'empty':
        S = set()

