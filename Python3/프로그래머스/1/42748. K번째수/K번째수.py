# i, j, k
# i-1에서 j까지 슬라이싱
# 슬라이싱된 리스트의 k-1 인덱스값 return

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        temp = array[commands[i][0]-1 : commands[i][1]]
        temp.sort()
        answer.append(temp[commands[i][2]-1])
        
    return answer