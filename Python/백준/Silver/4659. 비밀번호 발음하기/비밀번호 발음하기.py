from sys import stdin as s 

con = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vow = ['a', 'e', 'i', 'o', 'u']

while True:
    pw = s.readline().strip()

    if pw == 'end':
        break

    # case #1
    if any(i in pw for i in vow):
        acceptable = 1
    else:
        acceptable = 0
    
    # case #2
    for i in range(len(pw)-2):
        word = pw[i] + pw[i+1] + pw[i+2]

        if all(i in vow for i in word) or all(i in con for i in word):
            acceptable = 0 
            break
        else:
            acceptable = 1
    
    # case #3
    is_same = False 
    same_word = ''
    front_word = ''

    for i in pw:
        if i == front_word:
            same_word = i+front_word
            if same_word == 'ee' or same_word == 'oo':
                acceptable = 1
            else:
                is_same = True
                break 
            
        front_word = i

    if is_same == True:
        acceptable = 0

    if acceptable == 0:
        print(f'<{pw}> is not acceptable.')
    else:
        print(f'<{pw}> is acceptable.')

    