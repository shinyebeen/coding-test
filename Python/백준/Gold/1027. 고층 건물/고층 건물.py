from sys import stdin as s

n = int(s.readline())
height = list(map(int, s.readline().rstrip().split()))
answer = [0] * n

for i in range(n-1):
    max_slope = -float('inf')
    for j in range(i+1, n):
        slope = (height[j] - height[i]) / (j-i)
        if slope <= max_slope:
            continue 
        max_slope = max(max_slope, slope)
        answer[i] += 1
        answer[j] += 1

print(max(answer))