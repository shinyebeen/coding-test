# from itertools import product
def solution(word):
    
    d = ['A','E','I','O','U']
    directory = []
    for i in d:
        directory.append(i)
        for j in d:
            directory.append(i+j)
            for k in d:
                directory.append(i+j+k)
                for l in d:
                    directory.append(i+j+k+l)
                    for n in d:
                        directory.append(i+j+k+l+n)
    directory.sort()
    
    return directory.index(word)+1