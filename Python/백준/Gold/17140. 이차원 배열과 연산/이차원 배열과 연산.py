# C 연산 : 2차원 배열을 Transpose -> R 연산 수행 -> 배열 Transpose

from collections import Counter 
from functools import reduce 

## R연산
def R(array):
    mx = 0 # 가장 긴 리스트 길이
    for i in range(len(array)):
        X = Counter(array[i])
        del X[0] # 수를 정렬할 때, 0은 제외
        X = list(X.items())
        X.sort(key=lambda x:(x[1], x[0]))
        if len(X) > 50: X = X[:50] # 크기가 100을 넘으면 안됨
        array[i] = reduce(lambda x, y : list(x) + list(y), X[1:], list(X[0]))
        mx = max(mx, len(array[i]))

    ## 가장 긴 리스트에 맞춰 0 추가
    for i in range(len(array)):
        if len(array[i]) < mx:
            array[i].extend([0] * (mx - len(array[i])))

def main():
    r, c, k = map(int, input().split())
    r, c = r-1, c-1

    board = [list(map(int, input().split())) for _ in range(3)]
    time = 0 # 시간
    if r < len(board) and c < len(board[0]):
        if board[r][c] == k:
            return time 
    
    while True:
        if len(board) >= len(board[0]): # 행의 개수 >= 열의 개수, R연산
            R(board)
        else:
            board = list(map(list, zip(*board))) # 트랜스포즈
            R(board)
            board = list(map(list, zip(*board))) # 트랜스포즈
        time += 1
        if time > 100:
            return -1 
        if r < len(board) and c < len(board[0]):
            if board[r][c] == k:
                return time

print(main())