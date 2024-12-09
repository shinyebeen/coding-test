from collections import deque

def right(idx, d):
    if idx > 3:
        return 
    if cog[idx][6] != cog[idx-1][2]:
        right(idx+1, -d)
        cog[idx].rotate(d)

def left(idx, d):
    if idx < 0:
        return 
    if cog[idx][2] != cog[idx+1][6]:
        left(idx-1, -d)
        cog[idx].rotate(d)

cog = [deque(list(map(int, input()))) for _ in range(4)]
k = int(input())

for _ in range(k):
    idx, d = map(int, input().split())
    idx -= 1

    left(idx-1, -d)
    right(idx+1, -d)
    
    cog[idx].rotate(d)
    
score = 0
for i in range(4):
    if cog[i][0] == 1:
        score += 2**i 

print(score)