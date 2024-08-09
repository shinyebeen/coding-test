from sys import stdin as s 

N = int(s.readline().strip())

line = [list(s.readline().strip()) for _ in range(N)]
heart = []

for i in range(N):
    for j in range(N):
        if line[i][j] == '*' and len(heart) == 0:
            heart.append(i+1)
            heart.append(j)
            print(heart[0]+1, heart[1]+1)
            break 

# left arm
print(line[heart[0]][:heart[1]].count('*'), end=' ')

# rignt arm
print(line[heart[0]][heart[1]+1:].count('*'), end=' ')
    
# waist
cnt = 0  
for i in range(heart[0]+1, N):
    if line[i][heart[1]] == '*':
        cnt += 1
    else:
        leg = i
        break 
print(cnt, end=' ')

# left leg
cnt = 0  
for i in range(leg, N):
    if line[i][heart[1]-1] == '*':
        cnt += 1
    else:
        break 
print(cnt, end=' ')

# right arm
cnt = 0  
for i in range(leg, N):
    if line[i][heart[1]+1] == '*':
        cnt += 1
    else:
        break 
print(cnt, end=' ')
        