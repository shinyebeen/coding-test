from itertools import combinations

n, s = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
    comb_nums = combinations(nums, i)

    for j in comb_nums:
        if sum(j) == s:
            cnt += 1

print(cnt)