n = int(input())
arr = list(map(int, input().split()))
visited = [0] * 100001
answer = 0

start, end = 0, 0

while start <= end and end < n:
    if not visited[arr[end]]:
        visited[arr[end]] = 1
        end += 1
        answer += end-start
    else:
        while visited[arr[end]]:
            visited[arr[start]] = 0
            start += 1

print(answer)