from sys import stdin as s 

n = int(s.readline())

word = [s.readline().rstrip() for _ in range(n)]
word_sort = sorted(enumerate(word), key=lambda x:x[1])

def check(a, b):
    cnt = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            cnt += 1
        else:
            break 
    return cnt

length = [0] * n
max_length = 0

for i in range(n-1):
    tmp = check(word_sort[i][1], word_sort[i+1][1])
    max_length = max(max_length, tmp)

    length[word_sort[i][0]] = max(length[word_sort[i][0]], tmp)
    length[word_sort[i+1][0]] = max(length[word_sort[i+1][0]], tmp)

first = 0
for i in range(n):
    if first == 0:
        if length[i] == max(length):
            first = word[i]
            print(first)
            pre = word[i][:max_length]
    else:
        if length[i] == max(length) and word[i][:max_length] == pre:
            print(word[i])
            break