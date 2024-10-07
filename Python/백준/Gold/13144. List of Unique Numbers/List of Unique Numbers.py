from sys import stdin as s 

n = int(s.readline())
arr = list(map(int, s.readline().rstrip().split()))
visited = [0] * 100001
answer = 0

start = 0
end = 0

while start <= end and end < n:
    if not visited[arr[end]]:        # end 위치가 false면 if문 수행
        visited[arr[end]] = 1
        end += 1
        answer += end-start
    else:
        while visited[arr[end]]:     # start를 end 위치까지 이동시키면서 false으로 바꿈
            visited[arr[start]] = 0
            start += 1

print(answer)