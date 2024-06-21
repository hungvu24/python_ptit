t = int(input())
while t > 0 :
    s = input()
    l = len(s)
    if s[0] == s[l-2] and s[1] == s[-1] :
        print("YES")
    else :
        print("NO")
    t -= 1