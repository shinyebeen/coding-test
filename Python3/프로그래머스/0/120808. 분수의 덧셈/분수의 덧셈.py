import math

def solution(numer1, denom1, numer2, denom2):
    a = denom1 * denom2
    b = numer1 * denom2 + numer2 * denom1
    
    #gcd : 최대공약수
    gcd = math.gcd(a,b)
    
    a //= gcd
    b //= gcd

    return [b, a]