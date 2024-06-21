t = int(input())
def check(s):
    for i in range(2 , len(s)):
        if s[i]  != s[i-2]:
            return 'NO'
    return 'YES'
while t > 0:
    s = input()
    print(check(s))
    t -= 1