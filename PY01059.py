t = int(input())
while t > 0 :
    s = input()
    sum = 0
    tich = 1
    le = False
    for i in range ( 0 , len(s) , 2):
        sum += int(s[i])
    for i in range(1 , len(s) , 2):
        if int(i) != 0:
            tich *= int(s[i])
            le = True
    if not le :
        tich = 0
    print(sum , tich , end=' ')

    t -= 1
