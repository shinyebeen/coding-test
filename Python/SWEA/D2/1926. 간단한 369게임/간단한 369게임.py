n = int(input())
answer = []

for i in range(1, n+1):
    clap = ''
    for s in str(i):
        if s=='3' or s=='6' or s=='9':
            clap += '-'

    if len(clap)>0:
	    answer.append(clap)
    else:
        answer.append(i)

print(*answer)