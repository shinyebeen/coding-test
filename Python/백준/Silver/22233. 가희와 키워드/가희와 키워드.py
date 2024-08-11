from sys import stdin as s

n, m = map(int, s.readline().strip().split())

keyword = set(s.readline().strip() for _ in range(n))

for i in range(m):
    blog = set(s.readline().strip().split(','))
    keyword -= blog
    
    print(len(keyword))