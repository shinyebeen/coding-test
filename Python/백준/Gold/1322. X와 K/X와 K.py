# K가 최대 2억이므로 브루트포스는 못 씀
# 비트마스크 활용
# x의 0에 해당하는 y 부분을 보면 k의 2진수 표현과 동일함
# => k번째 y값을 구하기 위해서는 x에서 0에 해당하는 자리에 k 2진수 표현을 넣어주면 됨
# 참고 : https://everenew.tistory.com/75 

x,k = map(int,input().split())
k = list(bin(k)[2:])
x = list(bin(x)[2:])
ans = ""
while k:
    if x:
        a = x.pop()
        if a == "1":
            ans += "0"
        else:
            ans += k.pop()
    else:
        ans += k.pop()

print(int("0b"+ans[::-1],2))