N, M = map(int, input().split())
board = [[] for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))
blizard = [[] for _ in range(M)]
for i in range(M):
    blizard[i] = list(map(int, input().split()))
shark = [(N - 1) // 2, (N - 1) // 2]
result = [0, 0, 0]


def destroy(d, s):
    global board, N, shark

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(1, s + 1):
        nx = shark[0] + dx[d - 1] * i
        ny = shark[1] + dy[d - 1] * i

        # 격자를 넘어가면 continue
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            break

        # 파괴
        board[nx][ny] = 0


def board2list():
    global board

    arr = []
    cur = shark[:]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    num = 1
    direction = 0
    is_over = False
    while not is_over:
        for i in range(2):
            for j in range(num):
                cur[0] += dx[direction]
                cur[1] += dy[direction]

                # 격자 밖으로 넘어간다면
                if cur[0] < 0 or cur[1] < 0 or cur[0] >= N or cur[1] >= N:
                    is_over = True
                    break

                # 회오리 순서대로 배열에 append
                arr.append(board[cur[0]][cur[1]])
            direction = (direction + 1) % 4
            if is_over:
                break
        num += 1

    return arr


def move(arr):
    # 구슬 배열에서 빈칸 제거
    return [arr[i] for i in range(len(arr)) if arr[i] != 0]


def explode(arr):
    global result

    # 구슬이 존재하지 않는 경우
    if not arr:
        return [], False

    # 연속하는 구슬이 4개 이상이면 폭발
    cur_marble = arr[0]
    cur_num = 1
    is_removed = False

    for i in range(1, len(arr)):
        # 같은 색의 구슬이라면
        if arr[i] == cur_marble:
            cur_num += 1
        else:
            # 다른 색의 구슬인데 4개 미만인 경우
            if cur_num < 4:
                cur_num = 1
                cur_marble = arr[i]
            # 다른 색의 구슬인데 4개 이상인 경우
            else:
                # 개수만큼 이전 구슬들 폭발
                for j in range(1, cur_num + 1):
                    arr[i - j] = 0
                # result에 폭발 개수 저장
                result[cur_marble - 1] += cur_num
                is_removed = True
                # 새로운 색으로 update
                cur_num = 1
                cur_marble = arr[i]
    # 마지막으로 현재 구슬들 체크
    if cur_num >= 4:
        is_removed = True
        for j in range(1, cur_num + 1):
            arr[len(arr) - j] = 0
        result[cur_marble - 1] += cur_num

    return arr, is_removed


def make_group(arr):
    # 구슬이 존재하지 않는 경우
    if not arr:
        return []

    # 그룹으로 묶어서 [구슬 개수, 구슬 번호]로 변경
    new_arr = []
    cur_type = arr[0]
    cur_num = 1

    for i in range(1, len(arr)):
        # 같은 색의 구슬인 경우
        if arr[i] == cur_type:
            cur_num += 1
        else:
            # 다른 색의 구슬인 경우 그룹 [구슬 개수, 구슬 번호] 추가
            new_arr.append(cur_num)
            new_arr.append(cur_type)
            cur_num = 1
            cur_type = arr[i]
    # 마지막 그룹 체크
    new_arr.append(cur_num)
    new_arr.append(cur_type)

    return new_arr


def list2board(arr):
    global N, shark

    # list 를 회오리 모양 보드로 변경
    new_board = [[0 for _ in range(N)] for _ in range(N)]

    # 구슬이 없다면
    if not arr:
        return new_board

    cur = shark[:]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    num = 1
    direction = 0
    cur_arr = 0
    is_over = False
    while not is_over:
        for i in range(2):
            for j in range(num):
                cur[0] += dx[direction]
                cur[1] += dy[direction]

                # 격자 밖으로 넘어간다면
                if cur[0] < 0 or cur[1] < 0 or cur[0] >= N or cur[1] >= N:
                    is_over = True
                    break

                # 회오리 순서대로 보드에 append
                new_board[cur[0]][cur[1]] = arr[cur_arr]
                cur_arr += 1
                # 구슬이 더이상 없다면
                if cur_arr >= len(arr):
                    is_over = True
                    break
            if is_over:
                break
            direction = (direction + 1) % 4
        num += 1

    return new_board


def solution():
    global M, blizard, board, result

    for i in range(M):
        destroy(blizard[i][0], blizard[i][1])  # 방향, 거리
        arr = board2list()
        arr = move(arr)
        while arr:
            arr, is_removed = explode(arr)
            if not is_removed:
                break
            arr = move(arr)
        board = list2board(make_group(arr))

    print(result[0] + 2 * result[1] + 3 * result[2])


solution()