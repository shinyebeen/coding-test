n = int(input())
sand_map = [list(map(int, input().split())) for _ in range(n)]

result = 0
now = [n//2, n//2]

left = [[-2, 0, 0.02], [2, 0, 0.02], [-1, -1, 0.1],
        [-1, 0, 0.07], [-1, 1, 0.01], [0, -2, 0.05],
        [1, 0, 0.07], [1, -1, 0.1], [1, 1, 0.01], [0, -1, 0]]
right = [[x, -y, z] for x, y, z in left]
up = [[y, x, z] for x, y, z in left]
down = [[-y, x, z] for x, y, z in left]

rate = {'left':left, 'right':right, 'up':up, 'down':down}

def wind(move, dx, dy, direct):
    global result

    for _ in range(move):
        now[0] += dx
        now[1] += dy 

        # 퍼지는 모래양 누적
        spread = 0
        
        # 회오리 끝난 경우
        if now[0] < 0 or now[1] < 0:
            break 

        for rx, ry, r in rate[direct]:
            nx = now[0] + rx 
            ny = now[1] + ry 

            # 퍼지지 않고 남은 모래
            if r==0:
                sand = sand_map[now[0]][now[1]] - spread 
            else:
                sand = int(sand_map[now[0]][now[1]] * r)
            
            if 0<=nx<n and 0<=ny<n:
                sand_map[nx][ny] += sand 
            else:
                result += sand 
            
            spread += sand

for i in range(n):
    if i%2 == 0:
        wind(i+1, 0, -1, 'left')
        wind(i+1, 1, 0, 'down')
    else:
        wind(i+1, 0, 1, 'right')
        wind(i+1, -1, 0, 'up')

print(result)