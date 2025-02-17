from sys import stdin as s

n = int(s.readline().rstrip())
em = {}

for idx, i in enumerate(map(int, s.readline().rstrip().split())):
    if i in em:
        em[i].append(idx)
    else:
        em[i] = [idx]

def DFS(idx):

    if idx not in em:
        return 0

    res = []
    
    for i in em[idx]:
        res.append(DFS(i))
    
    res.sort(reverse=True)
    res = [res[i]+i+1 for i in range(len(em[idx]))]
    return max(res)

print(DFS(0))