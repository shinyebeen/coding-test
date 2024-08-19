from sys import stdin as s

n, k = map(int, s.readline().strip().split())
arr = list(map(int, s.readline().strip().split()))
cnt = [0] * (max(arr) + 1)

start, end, res = 0, 0, 0

while end < n:
    if cnt[arr[end]] < k:
        cnt[arr[end]] += 1
        end += 1
    else:
        cnt[arr[start]] -=1
        start += 1
    res = max(res, end-start)

print(res)