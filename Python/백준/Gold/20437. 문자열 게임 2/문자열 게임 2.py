from sys import stdin as s 
from collections import defaultdict

t = int(s.readline())

for _ in range(t):
    w = s.readline().rstrip()
    k = int(s.readline())
    
    cnt = defaultdict(list)
    
    for i in range(len(w)):
        if w.count(w[i]) >= k:
            cnt[w[i]].append(i)
            
    if not cnt:
        print(-1)
    else:
        small = 10000
        big = 1
        
        for alpha in cnt:
            for i in range(len(cnt[alpha])-k+1):
                length = cnt[alpha][i+k-1] - cnt[alpha][i] + 1
                
                small = min(small, length)
                big = max(big, length)
        
        print(small, big)