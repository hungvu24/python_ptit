t = int(input())
while t > 0:
    s = input()
    tich = 1
    for i in s:
        if i != '0':
            tich *= int(i)
    print(tich)
    t -= 1
