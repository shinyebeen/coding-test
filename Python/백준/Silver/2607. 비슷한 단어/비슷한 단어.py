from sys import stdin as s

n = int(s.readline().strip())
word = list(s.readline().strip() for _ in range(n))
res = 0

for idx in range(1, n):
    cnt = 0
    a = list(word[0]) if len(word[idx]) > len(word[0]) else list(word[idx])
    b = list(word[idx]) if len(word[idx]) > len(word[0]) else list(word[0])

    for i in a:
        if i in b:
            b[b.index(i)] = 0
            cnt += 1
    if cnt-1 == len(b) or cnt+1 == len(b) or cnt == len(b):
        res += 1

print(res)