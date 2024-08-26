from sys import stdin as s

S = list(s.readline().strip())
T = list(s.readline().strip())

answer = 0
def sub(S, T):
    global answer 

    if len(S) == len(T):
        if T == S:
            answer = 1
        return 

    if T[-1] == 'A':
        sub(S, T[:-1])
    if T[0] == 'B':
        sub(S, T[:0:-1])
        
sub(S, T)
print(answer)