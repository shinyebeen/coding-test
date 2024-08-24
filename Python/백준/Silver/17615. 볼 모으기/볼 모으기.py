n = int(input())
ball = input()

cnt = []

temp = ball.lstrip('R')
cnt.append(temp.count('R'))

temp = ball.lstrip('B')
cnt.append(temp.count('B'))

temp = ball.rstrip('R')
cnt.append(temp.count('R'))

temp = ball.rstrip('B')
cnt.append(temp.count('B'))

print(min(cnt))