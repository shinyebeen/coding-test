# 연속된 두 칸의 높이가 같은 경우 -> ok
# 현재 칸이 다음 칸과 두 칸 이상 차이가 나는 경우 -> break
# 현재 칸이 다음 칸보다 한 칸 큰 경우 -> 다음 칸부터 +l번째 칸에 있는 수가 모두 같은지 확인
# 현재 칸이 다음 칸보다 한 칸 작은 경우 -> 현재 칸부터 -l번째 칸에 있는 수가 모두 같은지 확인

n, l = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

def check(line, l):
    # visitied : 경사로 위치
    visited = [False for _ in range(n)]

    for i in range(0, n-1):
        # 연속된 두 칸의 높이가 같은 경우
        if line[i] == line[i+1]:
            continue
        # 현재 칸이 다음 칸과 두 칸 이상 차이가 나는 경우
        elif abs(line[i]-line[i+1]) > 1:
            return False
        # 현재 칸이 다음 칸보다 한 칸 큰 경우
        elif line[i] > line[i+1]:
            temp = line[i+1]
            # 다음 칸부터 +l번째 칸에 있는 수 확인 
            for j in range(i+1, i+l+1):
                if 0 <= j < n:
                    # 경사 놓을 위치의 높이가 하나라도 다르면
                    if temp != line[j]:
                        return False
                    # 높이는 다 같은데 이미 경사가 놓여진 곳이면
                    elif visited[j]:
                        return False
                    # 경사 놓기
                    visited[j] = True
                # 경사 길이가 범위 벗어나면
                else:
                    return False
        # 현재 칸이 다음 칸보다 한 칸 작은 경우
        else:
            temp = line[i]
            # 현재 칸부터 -l번째 칸에 있는 수 확인
            for j in range(i, i-l, -1):
                if 0 <= j < n:
                    # 경사 놓을 위치의 높이가 하나라도 다르면
                    if temp != line[j]:
                        return False
                    # 높이는 다 같은데 이미 경사가 놓여진 곳이면
                    elif visited[j]:
                        return False

                    visited[j] = True
                # 경사 길이가 범위 벗어나면
                else:
                    return False
    return True

answer = 0
# row check
for i in board:
    if check(i, l):
        answer += 1

# col check
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(board[j][i])
    if check(temp, l):
        answer += 1

print(answer)