n = input().upper()
n_set = list(set(n))
cnt = []

for i in range(len(n_set)):
    cnt.append(n.count(n_set[i]))

if cnt.count(max(cnt)) >= 2 :
    print("?")

else:
    print(n_set[cnt.index(max(cnt))])