# def solution(numbers, target):
#     answer = 0
#     leaves = [0]
#     for num in numbers:
#         tmp = []
#         for leaf in leaves:
#             tmp.append(leaf+num)
#             tmp.append(leaf-num)
#         leaves = tmp
    
#     for leaf in leaves:
#         if leaf == target:
#             answer += 1
#     return answer


# 1, 1, 1, 1, 1
# 처음 시작 +1, -1
# 다음 값부터 +x, -x 하기
def solution(numbers, target):
    
    ans = [0]
    
    for n in numbers:
        tmp = []
        
        for a in ans:
            tmp.append(a+n)
            tmp.append(a-n)
        
        ans = tmp
    
    answer = 0
    for a in ans:
        if a == target:
            answer += 1
    return answer
    
    