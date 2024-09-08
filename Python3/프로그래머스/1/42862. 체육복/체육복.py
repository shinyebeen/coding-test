# n : 전체 학생 수 2명 이상, 30명 이하
# lost : 도난 학생은 1명 이상, n명 이하
# reserve : 도난 학생이 여기에 포함될 수 있음 => 체육복 개수 하나라고 가정

# n 길이 리스트 생성 (1으로 초기화)
# reserve : 각 위치에 2 넣기
# lost : 각 위치 -1
# 앞 뒤 인덱스에 2 있으면 가져오고 -1시키기, 아니면 패쓰

# set.remove() : O(1)
# list.remove() : O(n)

def solution(n, lost, reserve):
    # lost와 reserve에 모두 포함돼있는 값 제거
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
            
    return n-len(set_lost)