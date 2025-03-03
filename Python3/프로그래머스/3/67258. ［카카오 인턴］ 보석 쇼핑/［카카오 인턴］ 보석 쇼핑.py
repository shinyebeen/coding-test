# 투 포인터로 확인

# set(gems)로 보석 개수 확인
# 딕셔너리로 각 보석 별 개수 저장하기

# start, end = 0, 0 에서 시작
# end += 1
# start != end인데 gems[start] == gems[end]라면 gems[start] != gems[end]일 때까지 start += 1
# 만약 모든 보석 개수가 1 이상이면 멈추고 start+1과 end+1 return하기 

def solution(gems):
    size = len(set(gems))
    cnt = {gems[0]:1}
    answer = [0, len(gems) - 1]
    start , end = 0, 0

    while start <= end and end < len(gems):
        if len(cnt) == size:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            if cnt[gems[start]] == 1:
                del cnt[gems[start]]
            else:
                cnt[gems[start]] -= 1
            start += 1

        else:
            end += 1
            if end == len(gems):
                break
            if gems[end] in cnt.keys():
                cnt[gems[end]] += 1
            else:
                cnt[gems[end]] = 1

    return [answer[0]+1, answer[1]+1]