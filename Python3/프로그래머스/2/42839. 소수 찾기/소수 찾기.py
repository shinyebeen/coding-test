import itertools

def solution(numbers):
    nums = list(numbers)
    temp = []
    answer = 0
    
    for i in range(1, len(numbers)+1):   
        temp += list(itertools.permutations(nums, i))  
    
    nums = [int(''.join(i)) for i in temp]
    nums = set(nums)
    
    for num in nums: 
        if num == 0 or num == 1:
            continue
        
        for j in range(2, int(num**(0.5))+1):
            if num % j == 0:
                break
        else:
            answer += 1
        
    
    return answer