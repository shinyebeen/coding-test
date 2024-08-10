from sys import stdin as s

n, k = map(int, s.readline().strip().split())
arr = list(s.readline().strip())
ans = 0

for i in range(n):
    if arr[i] == 'P':
        for j in range(max(i-k, 0), min(i+k+1, n)):
            if arr[j] == 'H':
                arr[j] = 1
                ans += 1
                break

print(ans)