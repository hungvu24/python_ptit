import math
def isPrime(s):
    if s < 2 :
        return False
    for i in range(2 , int(math.sqrt(s))+1 ):
        if s % i == 0:
            return False
    return True
def check(s):
    for i in s :
        if not isPrime(int(i)):
            return 'No'
    tong = sum([int(i) for i in s])
    num1 , num2 = s , s[::-1]
    if not isPrime(int(num1)) and not isPrime(int(num2)) and not isPrime(tong):
        return 'No'
    return 'Yes'
t = int(input())
while t > 0:
    s = input()
    print(check(s))
    t -= 1