def isPrime(n):
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False 
    return n != 1 

def isPalindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1] 

n = int(input())
while True:
    if isPrime(n) and isPalindrome(n):
        print(n)
        exit()
    n += 1