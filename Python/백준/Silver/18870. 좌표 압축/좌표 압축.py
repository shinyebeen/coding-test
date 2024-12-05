n = int(input())
arr = []
for i, num in enumerate(map(int, input().split())):
    arr.append([i, num])

arr.sort(key = lambda x : x[1])
arr[0] = arr[0] + [0]
idx = 0

for i in range(1, n):
    if arr[i][1] == arr[i-1][1]:
        arr[i].append(idx)
    else:
        idx += 1
        arr[i].append(idx)

arr.sort(key = lambda x : x[0])

for i in arr:
    print(i[2], end=' ')