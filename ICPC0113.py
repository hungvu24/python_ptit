import math
def isPrime(s):
    for i in range(2 , int(math.sqrt(s))+1 ):
        if s % i == 0:
            return False
    return s > 1
t = int(input())
while t > 0:
    n = int(input())
    use =[]
    for i in range(13 , n ):
        num = str(i)
        if int(num[::-1]) < n and num != num[::-1] and isPrime(int(num)) and isPrime(int(num[::-1])) and num not in use:
            print(i , num[::-1] , end = ' ')
            use +=[num , num[::-1]]
    print()
    t -= 1
