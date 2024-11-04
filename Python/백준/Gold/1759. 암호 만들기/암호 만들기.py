
def sol(depth, idx):
    vow, con = 0, 0

    if depth == l:
        # 모음, 자음 체크
        for i in password:
            if i in vowels:
                vow += 1
            else:
                con += 1

        if vow >= 1 and con >= 2:
            print(''.join(password))
        return

    for jdx in range(idx, c):
        password[depth] = alpha[jdx]
        sol(depth+1, jdx+1)

l, c = map(int, input().split())
alpha = input().split()
alpha.sort()

password = [0]*l
vowels = ['a', 'e', 'i', 'o', 'u']
sol(0, 0)