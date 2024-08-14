from sys import stdin as s
from collections import Counter 

S = list(s.readline().rstrip())
cnt_0 = S.count('0')
cnt_1 = S.count('1')

for i in range(cnt_1//2):
    S.remove('1')

S = S[::-1]

for i in range(cnt_0//2):
    S.remove('0')

print(''.join(S[::-1]))