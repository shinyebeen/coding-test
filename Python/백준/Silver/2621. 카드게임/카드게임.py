# 연속 여부 판단
def seq_num(li):
    li.sort()
    for i in range(len(li)-1):
        if li[i]+1 != li[i+1]:
            return False
    else:
        return True

# 같은 숫자 개수 세기
def same_num(li):
    cnt = []
    for i in li:
        cnt.append((li.count(i), i))

    cnt.sort(key=lambda x : (x[0], x[1]))
    answer = [cnt[-1], cnt[1]]
    
    return answer

color = set()
number = []

for _ in range(5):
    c, n = input().split()
    color.add(c)
    number.append(int(n))

# 색상이 모두 같을 경우
if len(color) == 1:
    # 숫자가 연속인가 ?
    if seq_num(number):
        print(max(number)+900)
    else:
        print(max(number)+600)
# 색상이 다른 경우
else:
    if seq_num(number):
        print(max(number)+500)
    else:
        same_number = same_num(number)
        if same_number[0][0] == 4:
            print(same_number[0][1]+800)
        elif same_number[0][0] == 3 and same_number[1][0] == 2:
            print(same_number[0][1]*10+same_number[1][1]+700)
        elif same_number[0][0] == 3 and same_number[1][0] == 1:
            print(same_number[0][1]+400)
        elif same_number[0][0] == 2 and same_number[1][0] == 2:
            print(same_number[0][1]*10+same_number[1][1]+300)
        elif same_number[0][0] == 2 and same_number[1][0] == 1:
            print(same_number[0][1]+200)
        else:
            print(max(number)+100)