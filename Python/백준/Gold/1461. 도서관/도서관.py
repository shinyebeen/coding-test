n, m = map(int, input().split())
position = list(map(int, input().split()))

pos, neg = [0], [0]

for i in position:
    if i > 0:
        pos.append(i)
    else:
        neg.append(-i)

pos.sort()
neg.sort()

max_num = max(pos[-1], neg[-1])
answer = 0


while pos:
    cnt = 0
    answer += pos[-1] * 2

    while pos and cnt < m:
        cnt += 1
        pos.pop()

while neg:
    cnt = 0
    answer += neg[-1] * 2

    while neg and cnt < m:
        cnt += 1
        neg.pop()

print(answer - max_num)
