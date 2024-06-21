t = int(input())
while t > 0:
    s = input()
    tong = 0
    tich = 1
    for i in range(0 , len(s), 2):
        if int(s[i]) != 0 :
            tich *= int(s[i])
    for i in range (1 , len(s),2):
        tong += int(s[i])
    print(tich , tong , end = ' ')
    print()
    t -= 1