# 원형조건 생각안하고 풀기
# 앞에서 시작, 뒤에서 시작 두 가지 모두 확인하기

def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    sticker_len = len(sticker)

    dp1 = [0] * sticker_len
    dp1[0] = sticker[0]
    dp1[1] = max(sticker[0], sticker[1])

    dp2 = [0] * sticker_len
    dp2[0] = 0
    dp2[1] = sticker[1] 

    # 첫 번째 스티커 사용 O
    for i in range(2, sticker_len - 1): 
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    # 첫 번째 스티커 사용 X
    for i in range(2, sticker_len):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    return max(dp1[sticker_len - 2], dp2[sticker_len - 1])