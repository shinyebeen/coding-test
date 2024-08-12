from sys import stdin as s

n, m = map(int, s.readline().rstrip().split())
word = {}

for _ in range(n):
    w = s.readline().rstrip()
    if len(w) < m:
        continue
    if w in word:
        word[w] += 1
    else:
        word[w] = 1

word = sorted(word.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

for w, _ in word:
    print(w)