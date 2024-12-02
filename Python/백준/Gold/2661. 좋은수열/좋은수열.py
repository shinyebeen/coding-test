n = int(input())

def dfs(res):
    if len(res) == n:
        print(''.join((map(str, res))))
        return True
    
    for i in range(1, 4):
        res.append(i)
        length = len(res)
        for size in range(1, length//2 + 1):
            if res[-size:] == res[-2*size:-size]:
                break
        else:
            if dfs(res):
                return True
                
        res.pop() # 수열 완성 안되면 pop

dfs([])