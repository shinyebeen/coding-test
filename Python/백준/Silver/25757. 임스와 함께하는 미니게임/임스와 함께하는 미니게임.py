from sys import stdin as s 

mini_game = {'Y':2, 'F':3, 'O':4}
n, game = s.readline().strip().split()
name = [s.readline().strip() for i in range(int(n))]

game = mini_game.get(game)-1 # 필요한 사람 수
done = set()
cnt = 0
res = 0
idx = 0

while idx < len(name):
    if name[idx] not in done:

        done.add(name[idx])

        cnt += 1

        if cnt == game:
            res += 1
            cnt = 0

    idx += 1

print(res)