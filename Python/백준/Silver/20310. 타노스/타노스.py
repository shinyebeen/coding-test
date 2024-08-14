from sys import stdin as s

from collections import Counter 

s = list(map(int, list(s.readline().rstrip())))
counter = list(Counter(s).items())
counter.sort(key=lambda x : x[0])

res = ''

for i in range(2):
    res += f'{counter[i][0]}'*(counter[i][1] // 2)

print(res)