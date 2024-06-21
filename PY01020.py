t = int(input())
while t > 0 :
    s = input()
    l = len(s)
    if s[l-1] == '6' and s[l-2] == '8':
        print('YES')
    else:
        print('NO')
    t -= 1