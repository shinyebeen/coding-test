from sys import stdin as s 

n = int(s.readline().strip())

for i in range(n):
    li = list(map(int, s.readline().strip().split()))
    test_case = li[0]
    student = li[1:]
    result = 0
    
    for j in range(20): 
        curr = student[j] 
        for k in range(j+1, 20): 
            if curr > student[k]: 
                result += 1 
    
    print(test_case, result) 