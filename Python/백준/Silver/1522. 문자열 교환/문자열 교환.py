from sys import stdin as s
from collections import deque

arr = list(s.readline().strip())

len_arr = len(arr)

start = 0
end = arr.count('a')
window = deque(arr[:end])

res = window.count('b')

while True:
    start = (start+1) % len_arr

    if start == 0:
        break 

    if res == 0:
        break
    
    window.popleft()
    window.append(arr[end])

    res = min(res, window.count('b'))

    
    end = (end+1) % len_arr 

print(res)
