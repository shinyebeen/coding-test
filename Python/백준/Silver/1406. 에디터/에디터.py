from sys import stdin as s

n1 = list(s.readline().rstrip())    # 커서 기준 왼쪽
n2 = []     # 커서 기준 오른쪽

m = int(s.readline().rstrip())

for _ in range(m):
    order = s.readline().rstrip().split()

    if order[0] == 'P':
        n1.append(order[1])
    elif order[0] == 'L':
        # n2에는 실제 n 순서와 반대되는 순서로 입력됨
        if n1:
            n2.append(n1.pop()) 
    elif order[0] == 'D':
        if n2:
            n1.append(n2.pop())
    else:
        if n1:
            n1.pop()

n1.extend(reversed(n2))
print(''.join(n1))