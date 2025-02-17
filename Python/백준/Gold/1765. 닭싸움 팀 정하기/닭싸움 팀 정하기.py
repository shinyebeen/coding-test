from sys import stdin as s

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if a < b:
        parent[b] = a 

    else:
        parent[a] = b

n = int(s.readline().rstrip())
m = int(s.readline().rstrip())
parent = [i for i in range(n+1)]
e = [[] for _ in range(n+1)]

for _ in range(m):
    r, p, q = s.readline().rstrip().split()
    p, q = int(p), int(q)
    
    if r == 'F':
        union(p, q)
    
    else:
        e[p].append(q)
        e[q].append(p)

for i in range(1, n+1):
    if len(e[i]) > 1:
        for j in range(1, len(e[i])):
            union(e[i][j-1], e[i][j])

ans = set()
for i in range(1, n+1):
    ans.add(find(i))
print(len(ans))