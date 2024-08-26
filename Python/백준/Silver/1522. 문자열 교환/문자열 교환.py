arr = list(input())
len_arr = len(arr)
cnt_a = arr.count('a')

arr = arr + arr
res = 1000

for i in range(len(arr) // 2):
    res = min(res, arr[i:i+cnt_a].count('b'))    

print(res)