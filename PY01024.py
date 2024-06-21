def check(s):
    if sum(int(i) for i in s) % 10 != 0:
        return 'NO'
    for i in range (len(s)-1):
        if abs(int(s[i]) - int(s[i+1])) != 2:
            return 'NO'
    return 'YES'
t = int(input())
while t > 0:
    n = input()
    print(check(n))
    t -= 1
