from sys import stdin as s

n = int(s.readline().strip())
pillar = []
res = 0

for i in range(n):
    l, h = map(int, s.readline().strip().split())
    pillar.append((l, h))

pillar.sort()

max_idx = 0
for i in range(n):
    if pillar[i][1] > pillar[max_idx][1]:
        max_idx = i

height = pillar[0][1]

for i in range(max_idx):
    if height < pillar[i+1][1]:
        res += height * (pillar[i+1][0] - pillar[i][0])
        height = pillar[i+1][1]
    else:
        res += height * (pillar[i+1][0] - pillar[i][0]) 

height = pillar[-1][1]

for i in range(n-1, max_idx, -1):
    if height < pillar[i-1][1]:
        res += height * (pillar[i][0] - pillar[i-1][0])
        height = pillar[i-1][1]
    else:
        res += height * (pillar[i][0] - pillar[i-1][0]) 

res += pillar[max_idx][1]
    
print(res)